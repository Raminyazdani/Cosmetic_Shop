from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from Products.models import Product, Category, Brand
from Costumers.models import Cart, CartItem
from Shops.models import Order, OrderItem
import decimal

User = get_user_model()

class MVPPagesTest(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Shops/home.html')

    def test_product_list_page(self):
        response = self.client.get(reverse('products:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Products/product_list.html')

class AuthTest(TestCase):
    def setUp(self):
        self.phone_number = '0912345678'
        self.password = 'testpass123'
        self.user = User.objects.create_user(phone_number=self.phone_number, password=self.password)

    def test_login(self):
        login = self.client.login(phone_number=self.phone_number, password=self.password)
        self.assertTrue(login)

    def test_register(self):
        response = self.client.post(reverse('cart:register'), {
            'phone_number': '0987654321',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        # Check if user was created and redirected
        self.assertTrue(User.objects.filter(phone_number='0987654321').exists())
        self.assertEqual(response.status_code, 302)

class ShopFlowTest(TestCase):
    def setUp(self):
        self.phone_number = '0912345678'
        self.password = 'testpass123'
        self.user = User.objects.create_user(phone_number=self.phone_number, password=self.password)
        self.client.login(phone_number=self.phone_number, password=self.password)
        
        self.category = Category.objects.create(name='Test Category')
        self.brand = Brand.objects.create(name='Test Brand')
        self.product = Product.objects.create(
            name='Test Product',
            price=decimal.Decimal('10.00'),
            short_description='A test product',
            is_available=True
        )
        self.product.category.add(self.category)
        self.product.brand.add(self.brand)

    def test_add_to_cart(self):
        response = self.client.post(reverse('cart:add', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CartItem.objects.count(), 1)
        self.assertEqual(CartItem.objects.first().product, self.product)

    def test_cart_update(self):
        cart = Cart.objects.create(user=self.user)
        item = CartItem.objects.create(cart=cart, product=self.product, quantity=1)
        
        response = self.client.post(reverse('cart:update', args=[item.id]), {'quantity': 5})
        self.assertEqual(response.status_code, 302)
        item.refresh_from_db()
        self.assertEqual(item.quantity, 5)

    def test_checkout(self):
        cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=cart, product=self.product, quantity=2)
        
        # Total price should be 20.00
        self.assertEqual(cart.total_price, decimal.Decimal('20.00'))
        
        response = self.client.post(reverse('cart:checkout'))
        self.assertEqual(response.status_code, 302)
        
        # Check if order was created
        self.assertEqual(Order.objects.count(), 1)
        order = Order.objects.first()
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.total_price, decimal.Decimal('20.00'))
        
        # Check if order items were created
        self.assertEqual(OrderItem.objects.count(), 1)
        order_item = OrderItem.objects.first()
        self.assertEqual(order_item.product, self.product)
        self.assertEqual(order_item.quantity, 2)
        
        # Check if cart was cleared
        self.assertEqual(CartItem.objects.filter(cart=cart).count(), 0)

    def test_empty_cart_checkout_redirect(self):
        response = self.client.get(reverse('cart:checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('cart', response.url)

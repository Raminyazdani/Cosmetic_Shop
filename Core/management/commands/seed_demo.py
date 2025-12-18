from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from Products.models import Category, Brand, Product, Tag
from Costumers.models import Cart, CartItem
from Shops.models import Address
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with demo data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding demo data...')

        # 1. Create Users
        admin_user, created = User.objects.get_or_create(
            phone_number='1234567890',
            defaults={
                'username': 'admin',
                'email': 'admin@example.com',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created superuser: {admin_user.phone_number}'))

        customer_user, created = User.objects.get_or_create(
            phone_number='0912345678',
            defaults={
                'username': 'customer',
                'email': 'customer@example.com',
                'is_costumer': True,
            }
        )
        if created:
            customer_user.set_password('customer123')
            customer_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created customer: {customer_user.phone_number}'))

        # 2. Create Categories
        categories = []
        for cat_name in ['Skincare', 'Makeup', 'Fragrance', 'Haircare']:
            cat, created = Category.objects.get_or_create(name=cat_name)
            categories.append(cat)
            if created:
                self.stdout.write(f'Created category: {cat_name}')

        # 3. Create Brands
        brands = []
        for brand_name in ["L'Oreal", "Estee Lauder", "MAC", "Clinique", "Nivea"]:
            brand, created = Brand.objects.get_or_create(name=brand_name)
            brands.append(brand)
            if created:
                self.stdout.write(f'Created brand: {brand_name}')

        # 4. Create Tags
        tags = []
        for tag_name in ['Organic', 'Vegan', 'Cruelty-Free', 'New', 'Best Seller']:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)
            if created:
                self.stdout.write(f'Created tag: {tag_name}')

        # 5. Create Products
        products_data = [
            ('Face Moisturizer', 'Hydrating face moisturizer for all skin types.', 25.99),
            ('Red Lipstick', 'Long-lasting matte red lipstick.', 15.50),
            ('Eau de Parfum', 'Luxury floral fragrance for women.', 85.00),
            ('Shampoo', 'Revitalizing shampoo with natural extracts.', 12.99),
            ('Eye Liner', 'Waterproof black liquid eye liner.', 10.00),
            ('Sunscreen SPF 50', 'High protection sunscreen for sensitive skin.', 18.00),
            ('Mascara', 'Volumizing black mascara.', 14.00),
            ('Foundation', 'Full coverage liquid foundation.', 32.00),
            ('Hair Mask', 'Deep conditioning treatment for dry hair.', 22.50),
            ('Night Cream', 'Anti-aging night cream with retinol.', 45.00),
        ]

        for name, desc, price in products_data:
            product, created = Product.objects.get_or_create(
                name=name,
                defaults={
                    'short_description': desc[:100],
                    'description': desc,
                    'price': price,
                    'is_available': True,
                    'gender': random.randint(0, 2),
                }
            )
            if created:
                # Assign random category, brand, and tags
                product.category.add(random.choice(categories))
                product.brand.add(random.choice(brands))
                product.tag.add(*random.sample(tags, k=random.randint(1, 3)))
                self.stdout.write(f'Created product: {name}')

        # 6. Create Address for customer
        address, created = Address.objects.get_or_create(
            name='Home Address',
            defaults={
                'slug': 'home-address'
            }
        )
        if created:
             self.stdout.write(f'Created default address')

        # 7. Create Cart and Items
        cart, created = Cart.objects.get_or_create(user=customer_user)
        if created:
            # Add some items to cart
            available_products = list(Product.objects.all()[:3])
            for p in available_products:
                CartItem.objects.create(cart=cart, product=p, quantity=random.randint(1, 2))
            self.stdout.write(self.style.SUCCESS(f'Created cart with items for {customer_user.phone_number}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded demo data!'))

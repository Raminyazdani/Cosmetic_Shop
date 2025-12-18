from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Cart, CartItem
from Products.models import Product
from Users.forms import UserRegistrationForm

# Create your views here.

def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome, {user.phone_number}')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def cart_view(request):
    """Display user's cart"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {
        'cart': cart,
        'cart_items': cart.items.all(),
    }
    return render(request, 'Costumers/cart.html', context)


@login_required
@require_POST
def cart_add(request, product_id):
    """Add product to cart"""
    product = get_object_or_404(Product, id=product_id, is_available=True, is_delete=False)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'Increased {product.name} quantity in cart.')
    else:
        messages.success(request, f'Added {product.name} to cart.')
    
    return redirect('cart:view')


@login_required
@require_POST
def cart_remove(request, item_id):
    """Remove item from cart"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f'Removed {product_name} from cart.')
    return redirect('cart:view')


@login_required
@require_POST
def cart_update(request, item_id):
    """Update cart item quantity"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, f'Updated {cart_item.product.name} quantity.')
    else:
        product_name = cart_item.product.name
        cart_item.delete()
        messages.success(request, f'Removed {product_name} from cart.')
    
    return redirect('cart:view')


@login_required
def checkout(request):
    """Simple checkout view"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if cart.items.count() == 0:
        messages.warning(request, "Your cart is empty.")
        return redirect('cart:view')
        
    if request.method == 'POST':
        # Create order from cart
        from Shops.models import Order, OrderItem, Address
        
        # Get or create a default address if none exists
        address = Address.objects.filter(is_delete=False).first()
        if not address:
            address = Address.objects.create(name="Default Address")

        order = Order.objects.create(
            user=request.user,
            name=f"Order for {request.user.phone_number}",
            total_price=cart.total_price,
            address=address
        )
        
        # Create order items from cart items
        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                name=cart_item.product.name,
                quantity=cart_item.quantity,
                price=cart_item.product.price
            )
        
        # Clear cart
        cart.items.all().delete()
        
        messages.success(request, f'Order placed successfully!')
        return redirect('cart:checkout_success')
    
    context = {
        'cart': cart,
        'cart_items': cart.items.all(),
    }
    return render(request, 'Costumers/checkout.html', context)


@login_required
def checkout_success(request):
    """Order confirmation page"""
    return render(request, 'Costumers/checkout_success.html')

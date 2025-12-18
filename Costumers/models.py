from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from Core.models import CoreModelUniversal
from Core.fields import ProjectFields

# Create your models here.

class Cart(CoreModelUniversal):
    """
    Shopping Cart Model
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name=_('User')
    )
    
    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')
    
    def __str__(self):
        return f"Cart for {self.user.username}"
    
    @property
    def total_items(self):
        return self.items.count()
    
    @property
    def total_price(self):
        return sum(item.subtotal for item in self.items.all())


class CartItem(CoreModelUniversal):
    """
    Cart Item Model
    """
    cart = models.ForeignKey(
        'Cart',
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name=_('Cart')
    )
    product = models.ForeignKey(
        'Products.Product',
        on_delete=models.CASCADE,
        verbose_name=_('Product')
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_('Quantity')
    )
    
    class Meta:
        verbose_name = _('Cart Item')
        verbose_name_plural = _('Cart Items')
        unique_together = ('cart', 'product')
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name}"
    
    @property
    def subtotal(self):
        return self.product.price * self.quantity

from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('subtotal',)
    fields = ('product', 'quantity', 'subtotal')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_items', 'total_price', 'created_at')
    readonly_fields = ('total_items', 'total_price', 'created_at', 'modified_at')
    inlines = [CartItemInline]
    search_fields = ('user__username', 'user__email')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'subtotal', 'created_at')
    list_filter = ('created_at',)
    readonly_fields = ('subtotal', 'created_at', 'modified_at')
    search_fields = ('cart__user__username', 'product__name')

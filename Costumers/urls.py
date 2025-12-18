from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='view'),
    path('add/<int:product_id>/', views.cart_add, name='add'),
    path('remove/<int:item_id>/', views.cart_remove, name='remove'),
    path('update/<int:item_id>/', views.cart_update, name='update'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/', views.checkout_success, name='checkout_success'),
    path('register/', views.register, name='register'),
]

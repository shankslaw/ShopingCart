from django.urls import path
from . import views

urlpatterns=[
    path('cart_details/',views.cart_details,name='cart_details'),
    path('add_to_cart/<int:product_id>',views.add_cart,name='add_to_cart'),
    path('decrement/<int:product_id>',views.min_cart,name='cart_decrement'),
    path('remove/<int:product_id>',views.cart_delete,name='remove'),
]
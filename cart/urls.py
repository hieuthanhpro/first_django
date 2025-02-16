from django.urls import path
from cart import views


urlpatterns = [
    path('add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_view, name='cart_view'),
]
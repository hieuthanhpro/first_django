from django.urls import path
from .views import register_customer, customer_list, update_customer, delete_customer

app_name = 'customer'  # Đặt namespace để gọi dễ dàng trong template

urlpatterns = [
    path('register/', register_customer, name='register'),
    path('list/', customer_list, name='list'),
    path('update/<int:customer_id>/', update_customer, name='update'),
    path('delete/<int:customer_id>/', delete_customer, name='delete'),
]

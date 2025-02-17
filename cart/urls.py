from django.urls import path
from cart import views

urlpatterns = [
    path('add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_view, name='cart_view'),
    path('update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),  # ✅ Thêm route này
    path('checkout/', views.checkout, name='checkout'),  # ✅ Thêm dòng này
]
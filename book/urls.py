from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),        # Trang danh sách sách
    path('new/', views.book_create, name='book_create'),  # Trang thêm sách
    path('<int:pk>/edit/', views.book_update, name='book_update'),  # Trang sửa sách
    path('<int:pk>/delete/', views.book_delete, name='book_delete'),  # Trang xóa sách
]

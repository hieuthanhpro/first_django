from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from book import models
@login_required(login_url='login')  # Nếu chưa đăng nhập, chuyển về login
def home(request):
    return render(request, 'homepage.html')
@login_required
def shop(request):
    books = models.Book.objects.all()
    return render(request, 'shop.html', {'books': books})
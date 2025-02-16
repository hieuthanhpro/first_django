from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Customer
from .forms import UserRegistrationForm, CustomerForm


def register_customer(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        customer_form = CustomerForm(request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            login(request, user)  # Đăng nhập ngay sau khi đăng ký
            return redirect('customer_list')  # Chuyển hướng về danh sách khách hàng
    else:
        user_form = UserRegistrationForm()
        customer_form = CustomerForm()
    return render(request, 'customer/register.html', {'user_form': user_form, 'customer_form': customer_form})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/list.html', {'customers': customers})


def update_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/update.html', {'form': form})


def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customer/delete.html', {'customer': customer})

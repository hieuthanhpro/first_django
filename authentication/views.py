# import this to require login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# import this for sending email to user
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from customer.models import Customer
from authentication.forms import UserRegistrationForm


# Create your views here.

@login_required(login_url='login')
def homepage(request):
    return render(request, 'homepage.html')


def register(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # Kích hoạt tài khoản ngay lập tức
            user.is_staff = False  # Chỉ superuser mới có thể tạo staff
            user.save()

            # Tạo Customer và liên kết với User
            Customer.objects.create(user=user)

            messages.success(request, 'Tạo tài khoản thành công! Chào mừng bạn.')
            return redirect('login')

        else:
            messages.error(request, 'Tạo tài khoản thất bại. Vui lòng thử lại.')

    return render(request, 'authentication/register.html', {'form': form})

# to activate user from email
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'authentication/email_activation/activation_successful.html')
    else:
        return render(request, 'authentication/email_activation/activation_unsuccessful.html')

@login_required(login_url='login')
def create_staff(request):
    if not request.user.is_superuser:
        messages.error(request, "Bạn không có quyền tạo staff!")
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Tên đăng nhập đã tồn tại!")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_staff = True
            user.save()
            messages.success(request, f"Tạo staff {username} thành công!")
            return redirect('home')

    return render(request, 'authentication/create_staff.html')
from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, Book

@login_required
def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    
    if book.stock > 0:
        cart_item, created = Cart.objects.get_or_create(customer=request.user.customer, book=book)
        cart_item.quantity += 1
        cart_item.save()

        book.stock -= 1  # Giảm số lượng sách tồn kho
        book.save()
    
    return redirect('book_list')
def cart_view(request):
    cart_items = Cart.objects.filter(customer=request.user.customer)
    total_price = sum(item.book.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'cart/cart.html', context)
def update_cart(request, item_id):
    """Cập nhật số lượng sản phẩm trong giỏ hàng."""
    if request.method == "POST":
        cart_item = get_object_or_404(Cart, id=item_id)
        new_quantity = request.POST.get("quantity")

        if new_quantity and int(new_quantity) > 0:
            cart_item.quantity = int(new_quantity)
            cart_item.save()
        else:
            cart_item.delete()  # Nếu số lượng <= 0 thì xóa khỏi giỏ hàng

    return redirect('cart_view')  # Chuyển hướng về trang giỏ hàng
def remove_from_cart(request, item_id):
    """Xóa sản phẩm khỏi giỏ hàng."""
    cart_item = get_object_or_404(Cart, id=item_id)
    cart_item.delete()
    
    return redirect('cart_view')  # Chuyển hướng về trang giỏ hàng
def checkout(request):
    """Xử lý thanh toán."""
    if not request.user.is_authenticated:
        return redirect('login')  # Nếu chưa đăng nhập thì về trang đăng nhập
    
    cart_items = Cart.objects.filter(customer=request.user.customer)
    total_price = sum(item.total_price() for item in cart_items)

    if request.method == "POST":
        # Xử lý đơn hàng tại đây (ví dụ: lưu vào Order model, xóa CartItem)
        cart_items.delete()
        return redirect('home')  # Sau khi checkout thành công, về trang chủ

    return render(request, 'cart/checkout.html', {'cart_items': cart_items, 'total_price': total_price})
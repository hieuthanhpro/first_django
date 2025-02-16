from django.shortcuts import redirect,render
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
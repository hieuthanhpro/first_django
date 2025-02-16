from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

# Hiển thị danh sách sách
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

# Thêm sách mới
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})

# Sửa thông tin sách
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_form.html', {'form': form})

# Xóa sách
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'book/book_confirm_delete.html', {'book': book})

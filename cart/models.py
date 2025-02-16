from django.db import models
from customer.models import Customer
from book.models import Book

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        """Tính tổng giá trị của mục trong giỏ hàng."""
        return self.quantity * self.book.price

    def __str__(self):
        return f"{self.quantity} x {self.book.title} ({self.customer.user.username})"

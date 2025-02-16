from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  # Số lượng tồn kho
    created_at = models.DateTimeField(auto_now_add=True)

    def is_available(self):
        """Kiểm tra xem sách có trong kho không."""
        return self.stock > 0

    def __str__(self):
        return f"{self.title} by {self.author}"

from django.contrib.auth.models import User
from django.db import models
from main_app.models import Shop


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)  # Optional for logged-in users
    session_id = models.CharField(max_length=100, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_id if self.session_id else str(self.user)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.product.title} ({self.quantity})"

    def get_total_price(self):
        return self.quantity * self.product.price

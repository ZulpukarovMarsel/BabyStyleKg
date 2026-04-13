from django.db import models
from accounts.models import User
from products.models import Product


class StatusOrder(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"StatusOrder(id={self.id}, title={self.title})"


class PaymentMethod(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"PaymentMethod(id={self.id}, title={self.title})"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    city = models.CharField(max_length=100)
    address = models.TextField()

    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(StatusOrder, on_delete=models.SET_NULL, null=True)

    delivery_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order(id={self.id})"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.title} x {self.quantity}"

    @property
    def total_price(self):
        return self.price * self.quantity

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import User


class Brand(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"Brand(id={self.id}, title={self.title})"


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"Category(id={self.id}, title={self.title})"


class AgeGroup(models.Model):
    title = models.CharField(max_length=50),
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"AgeGroup(id={self.id}, title={self.title})"


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.IntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    age_group = models.ForeignKey(AgeGroup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product(id={self.id}, title={self.title})"

    @property
    def in_stock(self):
        return self.stock > 0

    @property
    def final_price(self):
        return self.price * (1 - self.discount / 100)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/images/")

    def __str__(self):
        return f"ProductImage(id={self.id}, product-title={self.product.title})"


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

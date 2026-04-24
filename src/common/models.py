from django.db import models
from solo.models import SingletonModel
from django.core.validators import MinValueValidator, MaxValueValidator


class SiteSettings(SingletonModel):
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    instagram = models.URLField(blank=True)
    telegram = models.URLField(blank=True)

    delivery_text = models.TextField(blank=True)
    warranty_text = models.TextField(blank=True)

    def __str__(self):
        return "Настройки сайта"

    class Meta:
        verbose_name = "Настройки сайта"


class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner = models.ImageField(upload_to="site_images/")
    link = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"


class Review(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Отзыв от {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

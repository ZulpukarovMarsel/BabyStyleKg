from django.db import models
from solo.models import SingletonModel


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
    banner = models.ImageField(upload_to="banners/")
    link = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

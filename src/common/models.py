from django.db import models


class SiteSettings(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    instagram = models.URLField(blank=True)
    telegram = models.URLField(blank=True)

    delivery_text = models.TextField(blank=True)
    warranty_text = models.TextField(blank=True)

    def __str__(self):
        return "Site Settings"

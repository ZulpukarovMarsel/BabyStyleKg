from django.contrib import admin
from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    None


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    None

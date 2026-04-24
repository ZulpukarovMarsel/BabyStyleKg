import django_filters
from django_filters import BaseInFilter, CharFilter
from django.db import models
from .models import Product


class CharInFilter(BaseInFilter, CharFilter):
    pass


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    category = django_filters.CharFilter(field_name="category__slug")
    brands = CharInFilter(field_name='brand__slug', lookup_expr='in')
    ages = CharInFilter(field_name='age_group__slug', lookup_expr='in')
    search = django_filters.CharFilter(method='search_filter')
    sale = django_filters.BooleanFilter(method='filter_sale')

    class Meta:
        model = Product
        fields = []

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            models.Q(title__icontains=value)
        )

    def filter_sale(self, queryset, name, value):
        if value:
            return queryset.filter(discount__gt=0)
        return queryset

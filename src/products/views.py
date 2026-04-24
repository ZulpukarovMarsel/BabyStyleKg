from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, ProductImage, ProductReview, AgeGroup, Brand, Category
from .serializers import (
    ProductSerializer, ProductImageSerializer, ProductDetailSerializer, ProductReviewSerializer,
    AgeGroupSerializer, BrandSerializer, CategorySerializer
)
from .filters import ProductFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        return ProductDetailSerializer


class ProductReviewViewSet(ModelViewSet):
    serializer_class = ProductReviewSerializer

    def get_queryset(self):
        return ProductReview.objects.filter(product_id=self.kwargs['product_id'])

    def perform_create(self, serializer):
        serializer.save(product_id=self.kwargs['product_id'])


class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs['product_id'])


class AgeGroupViewSet(ModelViewSet):
    queryset = AgeGroup.objects.all()
    serializer_class = AgeGroupSerializer


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DiscountedProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(discount__gt=0)

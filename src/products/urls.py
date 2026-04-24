from django.urls import path
from .views import (
    ProductViewSet, ProductReviewViewSet, DiscountedProductViewSet,
    CategoryViewSet, BrandViewSet, AgeGroupViewSet
)


urlpatterns = [
    path('products/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),
    path('products/popular/', ProductViewSet.as_view({'get': 'list'})),
    path('products/discounted/', DiscountedProductViewSet.as_view({'get': 'list'})),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'}), name='product-retrieve'),
    path('products/<int:product_id>/reviews/', ProductReviewViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<int:product_id>/reviews/<int:pk>/', ProductReviewViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('products/category/', CategoryViewSet.as_view({'get': 'list'})),
    path('products/brands/', BrandViewSet.as_view({'get': 'list'})),
    path('products/age_group/', AgeGroupViewSet.as_view({'get': 'list'}))
]

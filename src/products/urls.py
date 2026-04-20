from django.urls import path
from .views import (
    ProductViewSet, ProductReviewViewSet, DiscountedProductViewSet,
    CategoryViewSet
)


urlpatterns = [
    path('products/', ProductViewSet.as_view({'get': 'list'})),
    path('products/popular/', ProductViewSet.as_view({'get': 'list'})),
    path('products/discounted/', DiscountedProductViewSet.as_view({'get': 'list'})),
    path('products/<int:product_id>', ProductViewSet.as_view({'get': 'retrieve'})),
    path('products/<int:product_id>/reviews/', ProductReviewViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<int:product_id>/reviews/<int:pk>/', ProductReviewViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('products/category/', CategoryViewSet.as_view({'get': 'list'}))
]

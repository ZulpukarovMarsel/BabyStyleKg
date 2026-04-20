from django.urls import path
from .views import (
    SiteSettingsViewSet, BannerViewSet
)


urlpatterns = [
    path('site_settings/', SiteSettingsViewSet.as_view({'get': 'list'})),
    path('banners/', BannerViewSet.as_view({'get': 'list'}))
]

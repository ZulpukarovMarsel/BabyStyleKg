from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import SiteSettings, Banner
from .serializers import SiteSettingsSerializer, BannerSerializer


class SiteSettingsViewSet(ModelViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer


class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

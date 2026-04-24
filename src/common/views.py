from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import SiteSettings, Banner
from .serializers import SiteSettingsSerializer, BannerSerializer


class SiteSettingsViewSet(ModelViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer

    def list(self, request, *args, **kwargs):
        obj = self.get_queryset().first()
        if not obj:
            return Response(
                {"detail": "Site settings not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(obj)
        return Response(serializer.data)


class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

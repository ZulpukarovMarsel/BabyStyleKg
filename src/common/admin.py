from django.contrib import admin
from .models import SiteSettings, Banner
from solo.admin import SingletonModelAdmin


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin):
    pass


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass

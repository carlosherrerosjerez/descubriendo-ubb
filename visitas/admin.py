from django.contrib import admin
from .models import VisitaPOI

class VisitAdmin(admin.ModelAdmin):
    list_display = ("user_id", "poi_id", "lat", "lng", "app_version", "timestamp")
    list_filter = ("poi_id", "app_version", "timestamp")
    search_fields = ("user_id", "poi_id")
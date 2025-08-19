from django.db import models

class VisitaPOI(models.Model):
    user_id = models.CharField(max_length=100)
    poi_id = models.CharField(max_length=100)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    app_version = models.CharField(max_length=50, blank=True, default="")
    ts_client = models.DateTimeField(null=True, blank=True)  # opcional
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} visitó {self.poi_id} en {self.timestamp}"

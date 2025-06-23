from django.db import models

class VisitaPOI(models.Model):
    user_id = models.CharField(max_length=100)
    poi_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} visitó {self.poi_id} en {self.timestamp}"

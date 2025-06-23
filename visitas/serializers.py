from rest_framework import serializers
from .models import VisitaPOI

class VisitaPOISerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitaPOI
        fields = '__all__'

from rest_framework import serializers
from .models import VisitaPOI

class VisitaPOISerializer(serializers.ModelSerializer):
    device_id = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = VisitaPOI
        fields = ['user_id', 'device_id', 'poi_id', 'lat', 'lng', 'app_version', 'ts_client', 'timestamp']
        read_only_fields = ['timestamp']

    def validate(self, attrs):
        if not attrs.get('user_id') and attrs.get('device_id'):
            attrs['user_id'] = attrs['device_id']
        if not attrs.get('user_id'):
            raise serializers.ValidationError({"user_id": "Se requiere user_id o device_id."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('device_id', None)
        return super().create(validated_data)

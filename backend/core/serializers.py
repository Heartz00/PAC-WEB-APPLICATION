from rest_framework import serializers
from .models import DICOMImage

class DICOMImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DICOMImage
        fields = ('id', 'file', 'uploaded_at')

from rest_framework import serializers
from .models import breast,lung

class breastSerializers(serializers.ModelSerializer):
    class Meta:
        model = breast
        fields = '__all__'

class lungSerializers(serializers.ModelSerializer):
    class Meta:
        model = lung
        fields = '__all__'

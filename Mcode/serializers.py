from rest_framework import serializers
from .models import Hero


#serializers here

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'
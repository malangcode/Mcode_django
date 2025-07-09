from rest_framework import serializers
from .models import HeroStats

#serializers here

class HeroStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroStats
        fields = '__all__'




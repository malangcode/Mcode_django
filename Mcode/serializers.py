from rest_framework import serializers
from .models import HeroStats, TeamMembers

#serializers here

class HeroStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroStats
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = '__all__'
    

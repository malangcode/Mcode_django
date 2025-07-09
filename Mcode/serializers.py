from rest_framework import serializers
from .models import HeroStats, TeamMembers, TimeLine

#serializers here

class HeroStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroStats
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = '__all__'
    


class TimeLineSerializers(serializers.ModelSerializer):
    class Meta:
        model = TimeLine
        fields = '__all__'
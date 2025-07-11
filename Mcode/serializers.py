from rest_framework import serializers
from .models import HeroStats, TeamMembers, TimeLine, ProjectCategory, Project


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
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = '__all__'

        
class ProjectSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.id')   
    class Meta:
        model = Project
        fields = '__all__'
        
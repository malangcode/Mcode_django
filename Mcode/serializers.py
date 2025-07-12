from rest_framework import serializers
from .models import HeroStats, TeamMembers, TimeLine, ProjectCategory, Project, Technologies, AboutFeatures, Services



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
        
        
        
class TechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologies
        fields = '__all__'

class AboutFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutFeatures
        fields = '__all__'
                
                
                
class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
                
                
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HeroStats, TeamMembers, TimeLine, ProjectCategory, Project, Technologies, AboutFeatures, Services, SocialLinks
from .serializers import HeroStatsSerializer, TeamMemberSerializer, TimeLineSerializers, CategorySerializer, ProjectSerializer, TechnologiesSerializer, AboutFeaturesSerializer, ServicesSerializer, SocialLinksSerializer





# Create your views here.

def home(request):
    return render(request, "index.html")


@api_view(['GET'])
def hero_stats(request):
    stats = HeroStats.objects.all().order_by('order')
    serializer = HeroStatsSerializer(stats, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def team_members(request):
    members = TeamMembers.objects.all()
    serializer = TeamMemberSerializer(members, many=True, context = {'request': request})
    return Response(serializer.data)
    

@api_view(['GET'])
def time_line(request):
    timeline = TimeLine.objects.all().order_by('order')
    serializer = TimeLineSerializers(timeline, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def project_categories(request):
    categories = ProjectCategory.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True, context = {'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def technologies(request):
    technologies = Technologies.objects.all()
    serializer = TechnologiesSerializer(technologies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def about_features(request):
    features = AboutFeatures.objects.all()
    serializer = AboutFeaturesSerializer(features, many=True)
    return Response(serializer.data)
    


@api_view(['GET'])
def services(request):
    services = Services.objects.all()
    serializer = ServicesSerializer(services, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def social_links(request):
    links = SocialLinks.objects.all()
    serializer = SocialLinksSerializer(links, many=True)
    return Response(serializer.data)


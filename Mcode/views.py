from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HeroStats, TeamMembers, TimeLine
from .serializers import HeroStatsSerializer, TeamMemberSerializer, TimeLineSerializers


# Create your views here.

def home(request):
    return HttpResponse("MalangCode Innovators Pvt Ltd")


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
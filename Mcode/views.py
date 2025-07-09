from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HeroStats
from .serializers import HeroStatsSerializer


# Create your views here.

def home(request):
    return HttpResponse("MalangCode Innovators Pvt Ltd")


@api_view(['GET'])
def hero_stats(request):
    stats = HeroStats.objects.all()
    serializer = HeroStatsSerializer(stats, many=True)
    return Response(serializer.data)



    


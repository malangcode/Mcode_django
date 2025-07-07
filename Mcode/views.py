from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hero
from .serializers import HeroSerializer


# Create your views here.

def home(request):
    return HttpResponse("MalangCode Innovators Pvt Ltd")


@api_view(['GET'])
def hero(request):
    heroes = Hero.objects.first()
    serializer = HeroSerializer(heroes, many=False)
    return Response(serializer.data)
    


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/stats/', views.hero_stats, name='stats'),
    path('api/team-members/', views.team_members, name='team_members'),
    path('api/time-line/', views.time_line, name='time_line'),
]

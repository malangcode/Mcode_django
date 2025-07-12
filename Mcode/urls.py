from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/stats/', views.hero_stats, name='stats'),
    path('api/team-members/', views.team_members, name='team_members'),
    path('api/time-line/', views.time_line, name='time_line'),
    path('api/project-categories/', views.project_categories, name='project_categories'),
    path('api/projects/', views.projects, name='projects'),
    path('api/technologies/', views.technologies, name='technologies'),
    path('api/about-features/', views.about_features, name='about_features'),
    path('api/services/', views.services, name='services'),
    path('api/social-links/', views.social_links, name='social_links'),
]

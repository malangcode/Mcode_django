from django.contrib import admin
from .models import HeroStats, TeamMembers, TimeLine, ProjectCategory, Project, Technologies, AboutFeatures, Services, Packages



# Register your models here.
@admin.register(HeroStats)
class HeroStatsAdmin(admin.ModelAdmin):
    list_display = ('label', 'number', 'icon')


@admin.register(TeamMembers)
class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')



@admin.register(TimeLine)
class TimeLineAdmin(admin.ModelAdmin):
    list_display = ('year', 'title')
    
    
@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    

@admin.register(Technologies)
class TechnologiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'icon')
    
@admin.register(AboutFeatures)
class AboutFeaturesAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title')    
    
    
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title', 'price', 'deliveryTime', 'projects')
    
    

@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color', 'popular')
    

    
    
    
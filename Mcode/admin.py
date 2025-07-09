from django.contrib import admin
from .models import HeroStats, TeamMembers


# Register your models here.
@admin.register(HeroStats)
class HeroStatsAdmin(admin.ModelAdmin):
    list_display = ('label', 'number', 'icon')


@admin.register(TeamMembers)
class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')


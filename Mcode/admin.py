from django.contrib import admin
from .models import HeroStats


# Register your models here.
@admin.register(HeroStats)
class HeroStatsAdmin(admin.ModelAdmin):
    list_display = ('label', 'number', 'icon')




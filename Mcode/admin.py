from django.contrib import admin
from .models import Hero

# Register your models here.



@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')


# Register your models here.

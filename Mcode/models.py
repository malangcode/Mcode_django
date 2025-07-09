from django.db import models

# Create your models here.
class HeroStats(models.Model):
    label = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)

    def __str__(self):
        return self.label
    

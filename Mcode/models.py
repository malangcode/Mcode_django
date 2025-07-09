from django.db import models

# Create your models here.
class HeroStats(models.Model):
    label = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.label
    
    
    
class TeamMembers(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    image = models.ImageField(upload_to="team_images/") 
    bio = models.TextField()
    skills = models.JSONField(default=list, blank=True)
    social = models.JSONField(default=dict, blank=True)
    
    def __str__(self):
        return f"Memeber: {self.name}"
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
    
    def __str__(self):
        return f"Memeber: {self.name}"
    

class TimeLine(models.Model): #this is time journey of our company in story section in about 
    year = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"In Year: {self.year} - {self.title}"
    
    
    

class ProjectCategory(models.Model): #filters
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField( max_length=200)    
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to="project_images/")
    technologies = models.JSONField(default=list)
    liveUrl = models.URLField(max_length=200)
    githubUrl = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title
    


class Technologies(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField()
    icon = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class AboutFeatures(models.Model):
    icon = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    

class Services(models.Model):
    icon = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    features = models.JSONField(default=list)
    price = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    deliveryTime = models.CharField(max_length=200)
    projects = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    
    
    
    








       
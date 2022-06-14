from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver #add this
from django.db.models.signals import post_save
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile', null=True)
    prof_image = models.ImageField(default='default.png', upload_to = 'profiles/')
    bio = models.CharField(max_length= 30)
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
        
    
        
    def __str__(self):
        return self.user.username


class Project(models.Model):
    proj_name= models.CharField(max_length=30)
    user = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name='projects',null=True)
    proj_description = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'projects/')
    pro_url = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
    def save_project(self):
        self.save()
    def delete_project(self):
        self.delete()
    @classmethod
    def all_projects(cls):
        projects = Project.objects.all()
        return projects
    @classmethod
    def search_project(cls, search_term):
        projects = cls.objects.filter(proj_name__icontains = search_term)
        return projects    
    def __str__(self):
        return self.proj_name
RATE_CHOICES = [
	(1, '1'),
	(2, '2'),
	(3, '3'),
	(4, '4'),
	(5, '5'),
	(6, '6'),
	(7, '7'),
	(8, '8'),
	(9, '9'),
	(10, '10'), 
]
   
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(max_length= 3000, blank=True)
    rate = models.PositiveIntegerField(choices= RATE_CHOICES)
    
    def __str__(self):
        return self.user.username
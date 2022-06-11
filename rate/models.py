from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    proj_name= models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    proj_description = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'projects/')
    pro_url = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
    def save_project(self):
        self.save()
    def delete_project(self):
        self.delete()
    
    def __str__(self):
        return self.proj_name
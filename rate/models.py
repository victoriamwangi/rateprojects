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
    
    # @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
    # def save_profile(sender, instance, created, **kwargs):
    #     user = instance
    #     if created:
    #         profile = Profile(user=user)
    #         profile.save()
    

    
    
    # @receiver(post_save, sender=User) #add this
	# def create_user_profile(sender, instance, created, **kwargs):
     
	# 	if created:
	# 		Profile.objects.create(user=instance)

	# @receiver(post_save, sender=User) #add this
    # def save_user_profile(sender, instance, **kwargs):
	# 	instance.profile.save()
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
    
    def __str__(self):
        return self.proj_name
    
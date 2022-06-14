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
    
    def save(self):
        self.save()

    def delete(self):
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
    averagerating=models.FloatField(default=0)
    
    
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

   
class Rate(models.Model):
    RATE_CHOICES = (
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
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='irate')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name= "ratings")
    design = models.IntegerField(choices=RATE_CHOICES, default=0,blank=False)
    content = models.IntegerField(choices=RATE_CHOICES, default=0,blank=False)
    usability = models.IntegerField(choices=RATE_CHOICES, default=0,blank=False)
    average = models.DecimalField(default=1, blank=False, decimal_places=2, max_digits=40)
    pub_date = models.DateTimeField(auto_now_add =True)
    
    def save(self):
        self.save()
    # @classmethod
    # def get_ratings(cls, id):
    #     ratings = Rate.objects.filter(post_id=id).all()
    #     return ratings
    @classmethod
    def get_project_rates(cls, id):
        votes = Rate.objects.all(id)
        return votes
    def __str__(self):
        return self.user.username
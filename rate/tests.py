from django.test import TestCase
from .models import Profile, Project
from django.contrib.auth.models import User


# Create your tests here.

class UserTest(TestCase):
    def setup(self):
        self.vicky = User(username = "vic", password= "hehe", email= "vic@gmail.com") 
        self.user.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.vicky, User))
class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username='vicky')
        self.user.save()
        self.vicprof = Profile(user = self.user, prof_image = "jpg", bio = "lets see", first_name = "vic", second_name= 'banks', location= "nairobi")
        self.vicprof.save_profile()  
    def test_instance(self):
        self.assertTrue(isinstance(self.vicprof, Profile ))
        
    def test_save_method(self):
        self.vicprof.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    def test_delete_method(self):
        self.vicprof.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)
        
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
class ProjectTest(TestCase):
    def setUp(self):
        self.project = Project(proj_name= "hello", proj_description = "world too", image = "jpg",pro_url = "url", pub_date = "22/2/22", averagerating = 34 )
        self.project.save_project()
    def test_instance(self):
        self.assertEqual(self.project, Project )
        
    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)
    def test_delete_method(self):
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)
        
    def tearDown(self):
        Project.objects.all().delete()
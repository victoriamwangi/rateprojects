from rest_framework import serializers
from .models import Profile, Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =Profile
        fields = ['id', 'user', 'prof_image', 'bio']
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model =Project
        fields = ['id', 'proj_name', 'proj_description', 'image', 'pro_url', 'pub_date', ]
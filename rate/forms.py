from .models import Profile, Project
from django import forms
from django.contrib.auth.models import User


class NewProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['proj_name', 'proj_description', 'image', 'pro_url']
        
class UpdateProfile(forms.ModelForm):
    class Meta:
        model= Profile
        exclude = ["user"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

    
    
    
from .models import Profile, Project
from django import forms


class NewProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['proj_name', 'proj_description', 'image', 'pro_url']
        
class UpdateProfile(forms.ModelForm):
    class Meta:
        model= Profile
        exclude = ["user"]
        
    
    
    
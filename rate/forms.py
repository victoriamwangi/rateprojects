from .models import Profile, Project,Review, RATE_CHOICES
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
class RateForm(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)
	rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)

	class Meta:
		model = Review
		fields = ('text', 'rate')
    
    
    
from django.shortcuts import render, redirect
from .forms import NewProject, UpdateProfile
from .models import Project, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render,get_object_or_404

# Create your views here.
def home(request):
    projects = Project.all_projects()
    return render(request,'home.html', {"projects": projects})

def new_project(request):
    user = request.user
    if request.method =='POST':
        form = NewProject(request.POST, request.FILES)
        if form.is_valid():
            project =form.save(commit=False)
            project.user = user
            form.save()
        return redirect('home')
    else:
        form = NewProject()
    return render(request, 'post_project/new_project.html', {'form': form})

def get_profile(request):    
    
    profile = get_object_or_404(Profile,user=request.user)
    
    return render(request,"profile.html",{"profile":profile})



def profile (request):
    user = request.user
    # projects = Profile.Project.all() 
    return render(request, 'profile/profile.html', )

@login_required(login_url='/accounts/login/')          
def update_profile(request):
    if request.method == 'POST':
        form= UpdateProfile(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit= False)
            form.instance.username.id = User.objects.get(username=request.user.id)
            post.save()
        return redirect('profile')
        
    else:
        form = UpdateProfile()
        return render(request, 'profile/update_profile.html', {"form": form})
            



        
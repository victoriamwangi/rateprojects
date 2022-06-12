from django.shortcuts import render, redirect
from .forms import NewProject
from .models import Project
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

def profile (request):
    user = request.user
    projects = user.profile.projects.all() 
    return render('profile/profile.html', {"projects": projects})


        
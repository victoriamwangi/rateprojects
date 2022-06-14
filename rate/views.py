from django.shortcuts import render, redirect
from .forms import NewProject, UpdateProfile, UserUpdateForm, RateForm
from .models import Project, Profile, Rate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.db.models import Avg

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
            project.user = user.profile
            form.save()
        return redirect('home')
    else:
        form = NewProject()
    return render(request, 'post_project/new_project.html', {'form': form})

def get_profile(request):    
    
    profile = get_object_or_404(Profile,user=request.user)
    
    return render(request,"profile.html",{"profile":profile})



def profile (request):
    projects = request.user.profile.projects.all() 
    return render(request, 'profile/profile.html',{"projects": projects} )


@login_required(login_url='/accounts/login/')          
def update_profile(request):
    if request.method == 'POST':
        profileform= UpdateProfile(request.POST, request.FILES, instance=request.user.profile)
        userUpdateform = UserUpdateForm(request.POST, instance=request.user)
        
        if profileform.is_valid() and userUpdateform.is_valid():
            profileform.save()
            userUpdateform.save()
            messages.success(request, f'Your account has been updated!')
            
        return redirect('profile')
        
    else:
        profileform = UpdateProfile( instance=request.user.profile)
        userUpdateform= UserUpdateForm(instance=request.user)
        return render(request, 'profile/update_profile.html', {"userUpdateform": userUpdateform, "profileform": profileform})
            
def search_project(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get('project')
        searched_project = Project.search_project(search_term)
        message = f'{search_term}'
        return render(request, 'search.html', {"message": message, 'projects':searched_project})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message': message})
    
    
def project_details(request, project_id):
    try:
        project = Project.objects.get(id = project_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"post_project/project.html", {"project": project})

def rate(request, project_id):
    project = Project.objects.get(id = project_id)
    rate = Rate.objects.filter(project = project)
    ratings = Rate.objects.all()
    rating_status = None
    if rate:
        rating_status = True
    else:
        rating_status = False
        
    if request.method == 'POST':
        rform = RateForm(request.POST)
        if rform.is_valid():
            design = rform.cleaned_data.get('design')
            usability = rform.cleaned_data['usability']
            content = rform.cleaned_data['content']
            rate = Rate()
            rate.project = project
            rate.user = request.user
            rate.design = design
            rate.usability = usability
            rate.content = content
            rate.average = (rate.design + rate.usability + rate.content) / 3
            rate.save()
            return HttpResponseRedirect(reverse('project_details', args=(project.id,)))
        else:
                
            rform = RateForm()
            params = {
            'project': project,
            'rform': rform,
            'rating_status': rating_status,
            'reviews': ratings,
            'ratings': rate
            }
        return render(request, "post_project/project.html", params)
  
        
   
    

# def rate(request, id):
#     project = Project.objects.get(id = id)
#     if request.method == 'POST':
#         rateform = RateForm(request.POST)
#         if rateform.is_valid():
#             rate = rateform.save(commit= False)
#             rate.user = request.user
#             rate.rating = request.POST["rating"]
#             rate.project = project
#             rate.save()
#         return  redirect('project-details',id)
#     else:
#         rateform = RateForm()
#         return render(request, "new_project/project.html", {"form": rateform})
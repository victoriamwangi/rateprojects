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

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer

# Create your views here.
def home(request):
    projects = Project.all_projects()
    return render(request,'home.html', {"projects": projects})

@login_required(login_url='/accounts/login/')          
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

@login_required(login_url='/accounts/login/')          
def get_profile(request):    
    
    profile = get_object_or_404(Profile,user=request.user)
    
    return render(request,"profile.html",{"profile":profile})

@login_required(login_url='/accounts/login/')          
def profile (request):
    projects = request.user.profile.projects.all() 
    return render(request, 'profile/profile.html',{"projects": projects} )


@login_required(login_url='/accounts/login/')          
def update_profile(request):
    
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profileform= UpdateProfile(request.POST, request.FILES, instance=request.user.profile)
        userUpdateform = UserUpdateForm(request.POST, instance=request.user)
        
        if profileform.is_valid() and userUpdateform.is_valid():
            profileform.save()
            userUpdateform.save()
            messages.success(request, f'Your account has been updated!')
            
        return redirect('profile',)

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
    

# def project_details(request, project_id):
#     try:
#         project = Project.objects.get(id = project_id)
#     except ObjectDoesNotExist:
#         raise Http404()
#     return render(request,"post_project/project.html", {"project": project})
    

@login_required(login_url='/accounts/login/')          
def project_details(request, project_id):
    form = RateForm()
    project = Project.objects.get(pk=project_id)
    rates = Rate.get_ratings(project.id)  
    total_rates = rates.count()
    rated = False
    
    raters_list =[]
    average_list = []
    content_list = []
    design_list = []
    usability_list = []
    for rate in rates:
        raters_list.append(rate.rater.id)
        average_summation = rate.design + rate.content + rate.usability
        average = average_summation/3
        average_list.append(average)
        content_list.append(rate.content)
        design_list.append(rate.design)
        usability_list.append(rate.usability)

        try:
            user = User.objects.get(pk = request.user.id)
            profile = Profile.objects.get(user = user)
            rater = Rate.get_project_raters(profile) #here
            voted = False
            if request.user.id in raters_list: 
                rated = True
        except Profile.DoesNotExist:
            rated = False    
  
    average_score = 0
    average_design = 0
    average_content = 0
    average_usability = 0
    if len(average_list) > 0:
        average_score = sum(average_list) / len(average_list)
        project.average_score = average_score
        project.save()  
    if total_rates != 0:
        average_design = sum(design_list) / total_rates
        average_content = sum(content_list) / total_rates
        average_usability = sum(usability_list) / total_rates
        project.average_design = average_design
        project.average_content =average_content
        project.average_usability = average_usability
        project.save()    

    return render(request, 'post_project/project.html', { "form": form, "project": project, "rates": rates, "rated": rated, "total_rates":total_rates})

class ProfileList(APIView):
    def get(self, request, format = None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many= True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format = None):
        all_projects= Project.objects.all()
        serializers = ProjectSerializer(all_projects, many= True)
        return Response(serializers.data)

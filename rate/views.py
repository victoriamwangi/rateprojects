from django.shortcuts import render, redirect
from .forms import NewProject, UpdateProfile, UserUpdateForm
from .models import Project, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages

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
    # projects = user.profile.projects.all() 
    return render(request, 'profile/profile.html', )
# {"projects": projects}
# def update_profile(request)
# @login_required
# def update(request):
#     if request.method == "POST":
#         updateform = UpdateProfile(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES,
#         instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Successfully updated your account!')
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, 'users/update.html', context)

@login_required(login_url='/accounts/login/')          
def update_profile(request):
    if request.method == 'POST':
        profileform= UpdateProfile(request.POST, request.FILES, instance=request.user.profile)
        userUpdateform = UserUpdateForm(request.POST, instance=request.user)
        
        if profileform.is_valid() and userUpdateform.is_valid():
            profileform()
            userUpdateform ()
            messages.success(request, f'Your account has been updated!')
            userUpdateform.save()
        return redirect('profile')
        
    else:
        profileform = UpdateProfile( instance=request.user.profile)
        userUpdateform= UserUpdateForm(instance=request.user)
        return render(request, 'profile/update_profile.html', {"userUpdateform": userUpdateform, "profileform": profileform})
            



        
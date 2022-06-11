from django.shortcuts import render, redirect
from .forms import NewProject
# Create your views here.
def home(request):
    return render(request,'home.html')

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
        
from django.urls import re_path, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    path('', views.home, name= 'home'),
    re_path('^new/project$', views.new_project, name= 'new-project'),
    re_path('^profile', views.profile, name= 'profile'),
    re_path(r'^update_profile/',views.update_profile,name = 'update'),
    re_path('search', views.search_project, name='search'),
    path('project/<int:project_id>)', views.project_details, name='project-details'),
    re_path(r'^api/profiles/$', views.ProfileList.as_view() ),
    re_path(r'^api/projects/$', views.ProjectList.as_view() )
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
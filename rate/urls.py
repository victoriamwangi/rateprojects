from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    re_path('^$', views.home, name= 'home'),
    re_path('^new/project$', views.new_project, name= 'new-project'),
    re_path('^profile', views.profile, name= 'profile'),
    re_path(r'^update_profile/',views.update_profile,name = 'update'),
    re_path('search', views.search_project, name='search')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.urls import path,re_path
#from django.conf.urls import url
from urlRender import views

urlpatterns = [
     re_path('^$',views.help,name='help'), 
     
]
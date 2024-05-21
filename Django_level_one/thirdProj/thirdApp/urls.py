from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.help,name='help'), # Include urls from mainApp
]
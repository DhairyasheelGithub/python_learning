from django.urls import path
from basic_app import views

#Template Tagging 
app_name = 'basic_app'

urlpatterns = [
    
    path('relatives/', views.relatives, name='relatives'),
    path('others/', views.others, name='others'),
    
]

from django.shortcuts import render
from basic_app import views
# Create your views here.

def index(request):
    text_dict = {'text':'Dhairyasheel Jamdade', 'number':100}
    return render(request, 'basic_app/index.html',text_dict)

def others(request):
    return render(request, 'basic_app/others.html')

def relatives(request):
    return render(request, 'basic_app/relative_url_templates.html') 


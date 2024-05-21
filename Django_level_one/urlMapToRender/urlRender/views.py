from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello! we are in Url Mapping")

def help(request):
    help_dict = {'help_me':'HELP PAGE'}
    return render(request,'help.html',context=help_dict)
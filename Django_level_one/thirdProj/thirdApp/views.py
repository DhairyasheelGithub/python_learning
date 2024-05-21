from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello")

def help(request):
    help_dict = {'insert_help':"HELP PAGE"}
    return  render(request, 'help.html', context=help_dict)
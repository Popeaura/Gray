#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
   # return HttpResponse ("Good Morning Africa! I'm Home")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse ("My About Page.") 
    return render(request, 'about.html')
 
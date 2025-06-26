from django.http import HttpResponse

def homepage(request):
    return HttpResponse ("Good Morning Africa! I'm Home")

def about(request):
    return HttpResponse ("My About Page.")
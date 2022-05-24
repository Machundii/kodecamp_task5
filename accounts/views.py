from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def signup(request):
    return HttpResponse("<h1>Sign Up Here </h1>"),

def login(request):
    return HttpResponse("<h1>Login Page</h1>")
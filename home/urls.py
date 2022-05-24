from django.urls import path
from .views import home, about, contact


urlpatterns = [ 
path("", home),
path("about-us/", about),
path("contact-us/", contact)
  ]



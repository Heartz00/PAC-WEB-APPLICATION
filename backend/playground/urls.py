from django.urls import path
from . import views

# URLconf - url configuration
urlpatterns = [
    path('hello/', views.say_hello)


]

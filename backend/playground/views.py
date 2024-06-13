from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# a function  that takes a request  and give a response, it is a request handler



def say_hello(request):
    
    # we can pull data from a database here
    # we can transform data, maybe we can even send email
    return render(request, 'hello.html', {'name': 'Ayomide'})


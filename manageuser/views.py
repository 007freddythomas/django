from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def reguser(request):
   return HttpResponse("<h1>Registration Page<h1>")

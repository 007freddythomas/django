from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def product(request):
    template = loader.get_template("productinfo.html")
    data={"name": "VIVO",
           "desc": " Smart Phone",
           "price": 45555}
    return HttpResponse(template.render(data,request))
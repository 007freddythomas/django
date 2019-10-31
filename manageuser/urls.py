from django.contrib import admin

from django.urls import path
from. views import reguser

urlpatterns = [
    path('register',reguser)
]
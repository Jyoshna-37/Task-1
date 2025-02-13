from django.contrib import admin
from django.urls import path, include
from .views import candidate_list

urlpatterns = [
    path('candidates/', candidate_list, name='candidate_list')
]
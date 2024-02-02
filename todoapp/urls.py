from . import views
from django.urls import path

urlpatterns = [
    path('', views.create_todo, name='create_todo'), 
]
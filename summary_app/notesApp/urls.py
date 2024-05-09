from django.urls import path
from notesApp import views
import django.contrib.auth.views as auth_views
urlpatterns = [
    
   

    path('notes/',views.list,name='allnotes'),
        path('makenotes/<str:subject_title>/<str:title>/<str:text>/',views.makenotes,name='makenotes'),

path('mynotes/<int:pk>/',views.detail, name='mynotes'),


]
from django.urls import include, path
from subjects import views
import django.contrib.auth.views as auth_views
urlpatterns = [

path('ai/', views.subject_ai, name='ai'),
path('cc/', views.subject_cc, name='cc'),

path('cn/', views.subject_cn, name='cn'),
path('daa/', views.subject_daa, name='daa'),
path('dbs/', views.subject_dbs, name='dbs'),
path('ml/', views.subject_ml, name='ml'),
path('os/', views.subject_os, name='os'),

path('dsa/', views.subject_dsa, name='dsa'),
path('se/', views.subject_se, name='se'),
path('oops/', views.subject_oops, name='oops'),
path('',include('notesApp.urls')),



]
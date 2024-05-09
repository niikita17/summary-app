from django.urls import include, path
from home import views
import django.contrib.auth.views as auth_views
urlpatterns = [
    path('',views.Home),
    path('home/',views.Home,name='Home'),
    path("registration/",views.registration, name='registration'),

 path('login_user/',views.login_user, name='login_user'),

        


path('logout/', views.logout_view, name='logout'),
path('subjects/',include('subjects.urls')),

]
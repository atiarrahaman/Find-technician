
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home , name='home'),
    path('login',views.Login , name='login'),
    path('signup',views.Signup , name='signup'),
    path('logout',views.Logout , name='logout'),
    path('mistriprofile',views.MistriProfile , name='mistriprofile'),
    path('editprofile',views.EditProfile , name='editprofile'),
    path('detailprofile/<int:id>',views.DetailsProfile , name='detailprofile'),
]

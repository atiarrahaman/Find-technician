
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home , name='home'),

    #signup And Login
    path('login',views.Login , name='login'),
    path('signup',views.Signup , name='signup'),
    path('logout',views.Logout , name='logout'),

   #for mistri
    path('mistriprofile',views.MistriProfile , name='mistriprofile'),
    path('editprofile',views.EditProfile , name='editprofile'),
    path('detailprofile/<int:id>',views.DetailsProfile , name='detailprofile'),
    #for tutor 
    path('tutorprofile',views.TutorProfile , name='tutorprofile'),
    path('tutoreditprofile',views.TutorProfileEdit , name='tutoreditprofile'),
    path('tutorshow',views.TutorShow , name='tutorshow'),
    path('tutordetails/<int:id>',views.TutorDetials , name='tutordetails'),
     #search
    path('search',views.Search , name='search'),
    
    # review
    path('reviews/',views.Review , name='reviews'),
    path('mistrireviews/',views.MistriReview , name='mistrireviews')
  
]

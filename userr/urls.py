from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register/', views.otp),
    path('register/reg/',views.register),
    path('update/',views.update),
    path('updatedonate/',views.updatedonate),
    path('updateloc/',views.updateloc),
    path('search/', views.searches),
    path('contact/', views.contact),
    path('about/', views.about),


]




  

from django.urls import path
from . import views
from .views import searchdisplay,donorlistdetail

urlpatterns = [
    path('', views.home),
    path('register/', views.otp),
    path('register/reg/',views.register),

  #  path('search/', views.search),
    path('contact/', views.contact),
    path('about/', views.about),
    path('display',views.display,name="display"),
   #path('searchbar/', views.searchbar,name="searchbar"),
    path('search/', searchdisplay, name='searchsite1'),
    path('list/', searchdisplay, name='donorlistsite'),
    path('register/information/<email>/', donorlistdetail, name='donorlistdetailsite'),
]




  

from django.urls import path,include
from seller import views

urlpatterns = [
    path('', views.home, name="home"),
    path('loginseller/',views.loginseller,name ='loginseller'),
    path('signupseller/',views.signupseller,name ='signupseller'),
    path('signoutseller/',views.logoutseller,name ='logoutseller'),
]
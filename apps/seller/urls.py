from django.urls import path,include
from seller import views

urlpatterns = [
    path('', views.home, name="home")
]

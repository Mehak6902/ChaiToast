from django.urls import path,include
from user import views

urlpatterns = [
    path('', views.home, name="home")
]
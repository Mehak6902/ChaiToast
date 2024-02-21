from django.urls import path,include
from user import views
from .views import  add_to_cart, view_cart, remove_from_cart
from django.conf import settings
from django.conf.urls.static import static


app_name = 'cart'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('home/', views.home, name="home"),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('loginuser',views.loginuser,name ='loginuser'),
    path('signupuser',views.signupuser,name ='signupuser'),
    path('logoutuser',views.logoutuser,name ='logoutuser'),
    path('contact',views.contact,name='contact'),
    path('about/', views.about_us, name='about'),



]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
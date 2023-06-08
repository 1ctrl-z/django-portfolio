from django.urls import path
from . import views

# This code is defining the URL patterns for a Django web application. It is creating two URL
# patterns:
urlpatterns = [
    path('', views.home_view, name="home"),
    path('register/', views.register, name='register'),

]

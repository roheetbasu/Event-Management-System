from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'events-home'),
    path('about/', views.about, name = 'events-about')
]
from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.author),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]

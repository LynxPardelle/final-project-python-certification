from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.author),
    path('chat/<str:type>/<int:id>', views.manageMessages),
]

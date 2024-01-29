from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.author),
    path('chat/<str:type>/<int:id>', views.manageMessages),
    path('chat/<str:type>', views.manageMessages),
    path('chat/<int:id>', views.manageMessages),
    path('chat', views.manageMessages),
]

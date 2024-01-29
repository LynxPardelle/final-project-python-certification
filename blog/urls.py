from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.author),
    path('pages/<str:option>/<int:id>/<str:search>', views.getBlogs),
    path('pages/<str:option>/<int:id>', views.getBlogs),
    path('pages', views.getBlogs),
    path('page/<str:option>/<int:id>/<str:search>', views.getBlogs),
    path('page/<str:option>/<int:id>', views.getBlogs),
    path('<str:option>/<int:id>/<str:search>', views.manipulateBlog),
    path('<str:option>/<int:id>', views.manipulateBlog, name="blog"),
    path('<str:option>', views.manipulateBlog),
    path('', views.getBlogs),
    path('img/<int:id>', views.uploadImage, name='uploadImage'),
]

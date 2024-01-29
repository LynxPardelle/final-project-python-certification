from django.urls import path
from . import views
urlpatterns = [
    path('author/', views.author),
    path('login', views.login_request, name="Login"),
    path('signup', views.register, name="Register"),
    path('logout', views.logout_request, name="Logout"),
    path('update_profile/<str:type>/<int:id>',
         views.updateUser, name="Update_profile"),
    path('update_profile/<int:id>',
         views.updateUser, name="Update_profile"),
    path('profile/<int:id>', views.getUser, name="Profile")
]

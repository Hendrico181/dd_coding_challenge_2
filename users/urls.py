from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [

    # Register a user
    path('register/', views.register, name='register'),

    # Authenticate a user
    path('my-login/', views.my_login, name='login'),

    # User logout
    path('my-logout/', views.my_logout, name='logout'),
]
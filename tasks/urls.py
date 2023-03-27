from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [

    # Dashboard page
    path('dashboard/', views.dashboard, name='dashboard'),

    # Logged in user's tasks
    path('self/', views.user_tasks, name='self'),

    # Create a task
    path('create-task/', views.create_task, name='create'),

    # Update a task
    path('edit/<int:task_id>/', views.update_task, name='update'),

    # Delete a task
    path('delete/<int:task_id>/', views.delete_task, name='delete'),

    # Change task status
    path('change-status/<int:task_id>/', views.change_status, name='change-status'),

    # View Tasks
    path('', views.index, name='list'),


]


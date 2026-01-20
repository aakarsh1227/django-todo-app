from django.urls import path
from . import views

urlpatterns = [ 
    # Main page showing the list
    path('', views.task_list, name='task_list'),
    
    # Backend action to toggle status (Complete/Incomplete)
    path('update-status/<int:pk>/', views.update_task_status, name="update_status"),
    
    # Backend action to delete
    path('delete-task/<int:pk>/', views.delete_task_backend, name="delete_task"),
]
from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('tasks/', task_list, name='task-list'),
    # path('tasks/<int:pk>/', task_detail, name='task-detail'),
    # path('tasks/<int:task_id>/items/', task_item_list, name='task-item-list'),
    # path('tasks/<int:task_id>/items/<int:pk>/', task_item_detail, name='task-item-detail'),
]
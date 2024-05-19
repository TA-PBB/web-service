from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskItemViewSet, register, CustomAuthToken

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'taskitems', TaskItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register, name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    
]
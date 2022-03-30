from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api_overview"),
    path('tasks/', views.task_list, name="tasks"),
    path('tasks/<str:pk>/', views.task_detail, name="task_detail"),
]
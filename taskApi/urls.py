from django.urls import path
from taskApi import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('get/<int:pk>', views.task, name='getTask'),
    path('add/', views.addTasks, name='add'),
    path('put/<int:pk>', views.EditTask, name='EditTask'),
    path('delete/<int:pk>', views.deleteTasks, name='delete'),
]
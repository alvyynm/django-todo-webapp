
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'task-home'),
    path('task<int:task_id>/', views.task_detail, name= 'task-details'),
    path('task<int:task_id>/update/', views.update, name="task-update"),
    path('tasks/', views.tasks, name= 'task-view'),
    path('addtask/', views.add, name= 'task-add'),
    path('about/', views.about, name= 'task-about'),
    path('contact/', views.contact, name= 'task-contact')
]
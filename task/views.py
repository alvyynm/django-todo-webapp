from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.

def home(request):
    return render(request, 'task/index.html')

def tasks(request):
    todos = Task.objects.all()
    context = {
        "tasks": todos
    }
    return render(request, 'task/tasks.html', context)
    # if request.method == 'POST':
    #     task = request.POST["task"]
    #     my_tasks.append(task)
    #     return render(request, 'task/tasks.html', {
    #         'my_tasks': my_tasks
    #     })
    # else:
    #     return render(request, 'task/tasks.html', {
    #         'my_tasks': my_tasks
    #     })
def add(request):
    return render(request, 'task/add.html')
    
def about(request):
    return render(request, 'task/about.html')

def contact(request):
    return render(request, 'task/contact.html')
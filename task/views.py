from django.shortcuts import render, redirect
from .models import Task
from .forms import ToDoForm

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

def task_detail(request, task_id):
    todo = Task.objects.get(id=task_id)
    context = {
        "todo": todo
    }
    return render(request, 'task/task_detail.html', context)

def add(request):
        form = ToDoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('task-view')  

        else:
                return render(request,'task/add.html', {"form": form})
    
def about(request):
    return render(request, 'task/about.html')

def contact(request):
    return render(request, 'task/contact.html')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

my_tasks = []

def home(request):
    return render(request, 'task/index.html')

def tasks(request):
    if request.method == 'POST':
        task = request.POST["task"]
        my_tasks.append(task)
        return render(request, 'task/tasks.html', {
            'my_tasks': my_tasks
        })
    else:
        return render(request, 'task/tasks.html', {
            'my_tasks': my_tasks
        })
def add(request):
    return render(request, 'task/add.html')
    
def about(request):
    return render(request, 'task/about.html')

def contact(request):
    return render(request, 'task/contact.html')
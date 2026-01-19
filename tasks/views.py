from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        # We explicitly set completed=True here
        Task.objects.create(title=title, completed=True) 
        return redirect('task_list')
    return render(request, 'tasks/todo.html', {'tasks': tasks})

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id) # Find the specific task
    task.completed = True               # Change status to True
    task.save()                         # Save changes to PostgreSQL
    return redirect('task_list')        # Go back to the main page
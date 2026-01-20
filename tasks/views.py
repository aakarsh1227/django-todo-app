from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title: # if empty tasks
            Task.objects.create(title=title)
        return redirect('task_list')
    
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/todo.html', {'tasks': tasks})


def update_task_status(request, pk):
    task = get_object_or_404(Task, id=pk)
    # This toggles the 'completed' status in the database
    task.completed = not task.completed 
    task.save()
    return redirect('/') # Sends you straight back to the list

# BACKEND DELETE: Deletes the item immediately
def delete_task_backend(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('/') # Sends you straight back to the list
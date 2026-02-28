from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            Task.objects.create(title=title, description=description)
    return redirect('task_list')

def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = 'Completed'
    task.save()
    return redirect('task_list')

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    pending_count = Task.objects.filter(status='Pending').count()
    completed_count = Task.objects.filter(status='Completed').count()
    total_count = Task.objects.count()

    context = {
        'tasks': tasks,
        'pending_count': pending_count,
        'completed_count': completed_count,
        'total_count': total_count,
    }

    return render(request, 'tasks/task_list.html', context)

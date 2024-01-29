from django.shortcuts import render, redirect, get_object_or_404

from task.models import Task


# Create your views here.
def add_task(request):
    task_name = request.POST.get("task_name")
    Task.objects.create(name=task_name)
    return redirect("home")


def remove_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect("home")


def mark_task_done(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_completed = True
    task.save()
    return redirect("home")


def mark_task_undone(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_completed = False
    task.save()
    return redirect("home")


def edit_task(request, pk):
    return render(request, "edit-task.html")

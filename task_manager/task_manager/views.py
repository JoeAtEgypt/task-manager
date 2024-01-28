from django.shortcuts import render

from task.models import Task


# Create your views here.
def home(request):
    uncompleted_tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)
    context = {
        "uncompleted_tasks": uncompleted_tasks,
        "completed_tasks": completed_tasks,
    }
    return render(request, "home.html", context=context)

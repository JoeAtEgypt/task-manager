from django.urls import path

from task import views

urlpatterns = [
    path("add/", views.add_task, name="add-task"),
    path("mark-task-done/<int:pk>", views.mark_task_done, name="mark-task-done"),
    path("remove/<int:pk>", views.remove_task, name="remove-task"),
]

from django.urls import path

from task import views

urlpatterns = [
    path("add/", views.add_task, name="add-task"),
    path("mark-task-done/<int:pk>", views.mark_task_done, name="mark-task-done"),
    path("mark-task-undone/<int:pk>", views.mark_task_undone, name="mark-task-undone"),
    path("remove/<int:pk>", views.remove_task, name="remove-task"),
]

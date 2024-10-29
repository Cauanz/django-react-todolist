from django.urls import path
from . import views

urlpatterns = [
   path("task/", views.TaskListCreateView.as_view(), name="list-create-task"),
   path("task/<int:pk>/", views.TaskRetrieverUpdateDestroyView.as_view(), name="delete-update-task")
]
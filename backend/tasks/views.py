from django.shortcuts import render
from api.serializers import TaskSerializer, TodoListSerializer
from .models import Task, ToDoList
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TodoListCreateView(generics.ListCreateAPIView):
   serializer_class = TodoListSerializer
   permission_classes = [IsAuthenticated]

   def get_queryset(self):
      return ToDoList.objects.filter(author=self.request.user)
   
   def create(self, serializer):
      serializer.save(author=self.request.user)

class TaskListCreateView(generics.ListCreateAPIView):
   serializer_class = TaskSerializer
   permission_classes = [IsAuthenticated]

   def get_queryset(self):
      return Task.objects.filter(todo_list__author=self.request.user)
   
   def create(self, serializer):
      todo_list = ToDoList.objects.get(id=self.request.data['todo_list'])
      serializer.save(todo_list=todo_list)

class TaskRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = TaskSerializer
   permission_classes = [IsAuthenticated]

   def get_queryset(self):
      return Task.objects.filter(todo_list__author=self.request.user)

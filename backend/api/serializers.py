from django.contrib.auth.models import User
from rest_framework import serializers
from tasks.models import Task, ToDoList

class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ["id", "username", "password"]
      extra_kwargs = {"password": {"write_only": True}}

   def create(self, validated_data):
      user = User.objects.create_user(**validated_data)
      return user

class TaskSerializer(serializers.ModelSerializer):
   class Meta:
      model = Task
      fields = ["content", "completed", "created_at", "author"]

class TodoListSerializer(serializers.ModelSerializer):
   tasks = TaskSerializer(many=True, read_only=True)

   class Meta:
      model = ToDoList
      fields = ['id', 'name', 'author', 'tasks']
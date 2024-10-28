from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
   name = models.CharField(max_length=130)
   author = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
      return self.name

class Task(models.Model):
   content = models.TextField(max_length=200)
   completed = models.BooleanField(default=False)
   created_at = models.DateTimeField(auto_now_add=True)
   todo_list = models.ForeignKey(ToDoList, related_name="tasks", on_delete=models.CASCADE)

   def __str__(self):
      return self.content
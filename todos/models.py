from django.db import models

# Create your models here.
class TodoList(models.Model):
    todoStatus = models.BooleanField(default=False)
    todoName = models.CharField(max_length=200)

    def __str__(self):
        return self.todoName
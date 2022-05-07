from enum import auto
from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=40)
    task_description = models.TextField()
    task_duedate = models.DateField()
    task_priority = models.IntegerField()

    def __str__(self):
        self.task_name
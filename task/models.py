# from enum import auto
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    task_name = models.CharField(max_length=40)
    task_description = models.TextField()
    task_duedate = models.DateField()
    task_priority = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.task_name

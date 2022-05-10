from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Task(models.Model):
    task_name = models.CharField(max_length=40)
    task_description = models.TextField()
    task_due_date = models.DateField()
    task_priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    # def __str__(self):
    #     self.task_name

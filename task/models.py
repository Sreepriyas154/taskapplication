from django.db import models

# Create your models here.
class Task(models.Model):
    taskname=models.CharField(max_length=200)
    user=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)

    def __str__(self) :
        return self.taskname
    
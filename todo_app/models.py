from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Task(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Done', 'Done')
    )
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS, default='Pending')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
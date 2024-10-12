
from django.db import models

# Create your models here.


class ToDo_list(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


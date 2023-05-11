from django.db import models

class ToDo(models.Model):
    user = models.CharField(max_length=100)
    task = models.CharField(max_length=150)
    done = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.task
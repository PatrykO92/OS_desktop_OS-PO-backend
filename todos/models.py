from django.db import models
from django.conf import settings

class ToDo(models.Model):
    task = models.CharField(max_length=150)
    done = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.task
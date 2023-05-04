from django.db import models
from django.conf import settings

class Score(models.Model):
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return '{self.user} = {self.score}'
from django.db import models
from django.conf import settings

class Score(models.Model):
    score = models.IntegerField()
    game_tag = models.CharField(max_length=15)
    

    def __str__(self) -> str:
        return f'{self.game_tag} = {self.score}'
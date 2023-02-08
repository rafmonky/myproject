from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    question4 = models.TextField()
    question5 = models.TextField()
    question6 = models.TextField()
    question7 = models.TextField()
    question8 = models.TextField()
    question9 = models.TextField()
    question10 = models.TextField()

    def highscore(self):
        score = models.PositiveIntegerField()


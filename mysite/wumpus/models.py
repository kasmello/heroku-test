from django.db import models

# Create your models here.

class Wumpus(models.Model):
    difficulty = models.TextField(default="Easy")

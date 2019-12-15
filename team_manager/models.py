from django.db import models

class Team(models.Model):
    # pk aka id --> numbers comes by default
    name        = models.CharField(max_length=120)
    timestamp   = models.DateTimeField(auto_now_add=True)

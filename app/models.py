from django.db import models

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    experience = models.IntegerField()

    def is_experienced(self):
        return self.experience >= 3
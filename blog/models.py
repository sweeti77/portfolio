from django.db import models
from datetime import date

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    posted_at = models.DateField(default=date.today)


    def __str__(self):
        return self.title
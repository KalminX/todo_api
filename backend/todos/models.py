from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def _str_(self):
        return self.title
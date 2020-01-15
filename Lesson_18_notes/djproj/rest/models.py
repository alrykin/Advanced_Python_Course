from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255, default=None)
    body = models.TextField(max_length=9186)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

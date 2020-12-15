from django.db import models

# Create your models here.
from django.db import models


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    DOB = models.DateField()
    email = models.EmailField(max_length=254)


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    ReleaseYear = models.CharField(max_length=50)
    Version = models.DecimalField(max_digits=3, decimal_places=2)
    author = models.ManyToManyField(Author, related_name='actor', through='Published')


class Published(models.Model):
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
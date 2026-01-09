from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')



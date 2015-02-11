from django.db import models


class Author(models.Model):
    name = models.TextField()


class Book(models.Model):
    author = models.ForeignKey("Author")
    title = models.TextField()

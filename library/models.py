from django.db import models


class Author(models.Model):
    name = models.TextField()


def image_upload_path(instance, filename):
    return "authors/%d/books/%d/%s" % (
        instance.author.pk,
        instance.pk,
        filename
    )


class Book(models.Model):
    author = models.ForeignKey("Author")
    title = models.TextField()
    cover = models.ImageField(null=True, blank=True,
                              upload_to=image_upload_path)

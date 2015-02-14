from django import forms
from django.contrib import admin
from library import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        exclude = ()

    def save(self, *args, **kwargs):
        book = super(BookForm, self).save(*args, **kwargs)
        book.title = "%s by %s (%d)" % (
            book.title,
            book.author.name,
            book.author.pk,
        )
        return book


class BookInline(admin.TabularInline):
    model = models.Book
    extra = 1
    form = BookForm


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]


admin.site.register(models.Author, AuthorAdmin)

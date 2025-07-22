from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    cover = models.ImageField(upload_to='book_covers/', blank=True, null=True)  # <-- вот это поле

    def __str__(self):
        return f"{self.title} by {self.author}"

from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.book_name
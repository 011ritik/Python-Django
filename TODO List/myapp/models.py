from django.db import models
from django.utils.text import slugify

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        # super() returns object to parent class
        return super().save(*args, **kwargs)

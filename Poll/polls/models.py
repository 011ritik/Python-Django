from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=300)
    pub_date = models.DateTimeField('pub_date')

class Choices(models.Model):
    question = models.ForeignKey(Question)
    choice = models.CharField(max_length=300)
    vote = models.IntegerField(default=0)
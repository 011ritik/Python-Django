from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=300)
    pub_date = models.DateTimeField('pub_date')

    def __str__(self):
        return self.question

class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    vote = models.IntegerField(default=0)


    
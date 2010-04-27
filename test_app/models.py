from django.db import models

class FirstModel(models.Model):
    char_field = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    text_field = models.TextField()
    integer_field = models.IntegerField()    

class SecondModel(models.Model):
    first_model = models.ForeignKey(FirstModel)


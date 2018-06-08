from django.db import models

# Create your models here.

class News(models.Model):
    name =models.CharField(max_length=200,db_column='name')
    link = models.CharField(max_length=256,db_column='link')

    class Meta:
        db_table = 'news'
from django.db import models

# Create your models here.
'''
Model field types:
models.models.CharField => varchar
models.IntegerField => int
models.DateField => date
models.ForeignKey => foreign key
'''
BALANCE_TYPE = (('收入','收入'),('支出','支出'))

class Category(models.Model):
    category = models.CharField(max_length = 20)

class Record(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cash = models.IntegerField()
    balance_type = models.CharField(max_length=2, choices=BALANCE_TYPE)



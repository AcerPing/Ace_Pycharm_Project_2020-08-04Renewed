from django.db import models

# Create your models here.
'''
Model field types:
models.models.CharField => varchar
models.IntegerField => int
models.DateField => date
models.ForeignKey => foreign key
'''
'''
Django ORM
Record.objects.get(id=1) -> 取得某一筆資料
Record.objects.filter(date_gte='2016-09-01') -> 取得某一範圍資料
Category.objects.create(category='娛樂') -> 新增一筆資料
Category.objects.filter(id=1).update(category='娛樂') -> 更新一筆資料
Category.objects.filter(id=1).delete() -> 刪除一筆資料
'''
BALANCE_TYPE = (('收入','收入'),('支出','支出'))

class Category(models.Model):
    category = models.CharField(max_length = 20)

    def __str__(self):
        return self.category

class Record(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cash = models.IntegerField()
    balance_type = models.CharField(max_length=2, choices=BALANCE_TYPE)

    def __str__(self):
        return self.description



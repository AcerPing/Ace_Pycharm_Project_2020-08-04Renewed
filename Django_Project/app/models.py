from django.db import models
from django.contrib.auth.models import User

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
'''
ForeignKey的on_delete參數
models.CASCADE
models.PROTECT
models.SET_NULL: 要搭配null=True
models.SET_DEFAULT: 要搭配default
models.SET(): 要傳入function
'''
BALANCE_TYPE = ((u'收入', u'收入'),(u'支出', u'支出'))

class Category(models.Model):
    category = models.CharField(max_length = 20)
    user = models.ForeignKey(User, null=True) #使用者

    def __str__(self):
        return self.category

class Record(models.Model):
    date = models.DateField() #日期
    description = models.CharField(max_length=300) #描述
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) #分類
    cash = models.IntegerField() #金額
    balance_type = models.CharField(max_length=2, choices=BALANCE_TYPE) #收支
    user = models.ForeignKey(User, null=True) #使用者

    def __str__(self):
        return self.description



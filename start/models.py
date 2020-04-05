from django.db import models

# Create your models here.
class Charge(models.Model):
    item = models.CharField(max_length=20)
    type_name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=5, decimal_places=0)
    in_out_come = models.CharField(max_length=10)

    class Meta:
        db_table = 'start_charge' # model使用的table名稱
        ordering = ['date'] # 排序 (-表示倒序)

class Category(models.Model):
    item_type = models.CharField(max_length=20)

    class Meta:
        db_table = 'type_category'
        ordering = ['item_type']
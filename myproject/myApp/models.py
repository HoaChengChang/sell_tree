from django.db import models
import datetime

class order(models.Model):
    firstname=models.CharField(max_length=20,verbose_name='姓氏')
    sex=models.CharField(max_length=20,verbose_name='性別')
    tex=models.CharField(max_length=20,verbose_name='電話')
    producttype=models.CharField(max_length=20,verbose_name='產品')
    count=models.CharField(max_length=20,verbose_name='數量')
    mailaddress=models.CharField(max_length=40,verbose_name='信箱')
    ps=models.TextField(max_length=100,default='',verbose_name='備註')
    dt=models.DateTimeField(max_length=40,verbose_name='訂購時間',auto_now_add=True)
    finished=models.BooleanField(default=False,verbose_name='完成處理')

    class Meta:
        verbose_name='訂購資訊'
        verbose_name_plural=verbose_name

class news(models.Model):
    title=models.CharField(max_length=20,verbose_name='標題')
    post_time=models.DateField(default=datetime.datetime.now,verbose_name='消息發送時間')
    text=models.TextField(max_length=250,null=True,verbose_name='內容')

    class Meta:
        verbose_name='最新消息'
        verbose_name_plural=verbose_name
 
class Product(models.Model):
    name=models.CharField(max_length=20,verbose_name='商品名稱')
    price=models.IntegerField(null=True,blank=True,verbose_name='價格')
    image=models.ImageField(null=True,blank=True,upload_to="media/")
    description=models.TextField(null=True,blank=True,verbose_name='描述')
    class Meta:
        verbose_name='產品'
        verbose_name_plural=verbose_name

class pic_display(models.Model):
    section=models.IntegerField(null=False,blank=False,verbose_name='段落')
    ordering=models.IntegerField(null=False,blank=False,verbose_name='照片順序')
    image=models.ImageField(null=False,blank=False,upload_to='media/')
    introd=models.CharField(max_length=10,null=True,blank=True,verbose_name='描述')
    class Meta:
        verbose_name='段落'
        verbose_name_plural=verbose_name

class PersonCount(models.Model):
    person_count=models.IntegerField(default=1,verbose_name='人數')
    class Meta:
        verbose_name='訪問人數'
        verbose_name_plural=verbose_name
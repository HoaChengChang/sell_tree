from django.shortcuts import render
from . import models
from . import signals
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import View
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.
def price_show(request):
    product=cache.get('product')
    if product is None:
        product=models.Product.objects.all()
        cache.set('product',product,60*60)
    context={}
    context['products']=product
    return render(request,"myApp/price.html",context)

# @cache_page(60*60)
def home(request):
    obj=models.PersonCount.objects.get_or_create(pk=1)
    if obj:
        total=obj[0].person_count+1
        models.PersonCount.objects.filter(pk=1).update(person_count=total)
    context={}
    all_news=cache.get('all_posts')
    all_pic=cache.get('all_pic')
    if all_news is None or all_pic is None:
        all_news=models.news.objects.all()
        all_pic=models.pic_display.objects.all()
        cache.set('all_posts',all_news,60*60)
        cache.set('all_pic',all_pic,60*60)

    context['all_posts']=all_news
    context['all_pic']=all_pic
    return render(request,"myApp/home.html",context)

def new_show(request,detail_id):
    context={}
    previousPage=0
    nextPage=0
    list=[]
    all_news=cache.get('all_news')
    if all_news is None:
        all_news=models.news.objects.all()
        cache.set('all_news',all_news,60*60)
        print(len(all_news))
    
    for all in all_news:
        
        list.append(str(all.id))
    
    if detail_id==int(list[0]) and len(list)!=1:
        previousPage=models.news.objects.get(pk=int(list[0]))
        nextPage=models.news.objects.get(pk=int(list[1]))
    elif detail_id==int(list[0]) and len(list)==1:
        previousPage=models.news.objects.get(pk=int(list[0]))
        nextPage=models.news.objects.get(pk=int(list[0]))
    elif detail_id==int(list[len(list)-1]):
        previousPage=models.news.objects.get(pk=detail_id-1)
        nextPage=models.news.objects.get(pk=detail_id)
    else :
        for i in len(list):
            if detail_id==list[i]:
                previousPage=models.news.objects.get(pk=int(list[i-1]))
                nextPage=models.news.objects.get(pk=int(list[i+1]))

    news=models.news.objects.get(pk=detail_id)
    context['news']=news
    context['previousPage']=previousPage
    context['nextPage']=nextPage
    return render(request,"myApp/news.html",context)

class order_(View):
    def get(self,request):
        context={}
        context['error']=''
        return render(request,"myApp/order.html",context)
    def post(self,request):
        context={}
        firstname=request.POST['firstname']
        sex=request.POST['sex']
        mailaddress=request.POST['mail']
        producttype=request.POST['producttype']
        count=request.POST['count']
        ps=request.POST['ps']
        tex=request.POST['tex']
        if not all([firstname,sex,mailaddress,producttype,count]):
            context['error']="輸入資料錯誤（空白)，請重新輸入"
            return render(request,"myApp/order.html",context)
        obj=models.order()
        obj.firstname=firstname
        obj.sex=sex
        obj.mailaddress=mailaddress
        obj.producttype=producttype
        obj.count=count
        obj.tex=tex
        obj.ps=ps
        obj.save()
        context['error']="訂購成功,近期會有專人與您聯繫"
        tmp=signals.order_signal.send(sender=None, firstname=firstname,sex=sex,mailaddress=mailaddress,producttype=producttype,count=count,tex=tex,ps=ps)
        if tmp is not None:
            context['error']=tmp[0][1]#return type [(memory_site,msg)]
        return render(request,"myApp/order.html",context)
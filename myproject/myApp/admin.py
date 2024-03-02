from django.contrib import admin
from .models import *
from .models import news,order,Product

@admin.register(order)
class useradmin(admin.ModelAdmin):
    list_display=['id','firstname','sex','tex','producttype','count','mailaddress','dt','finished']
    readonly_fields=['dt']
    list_filter=['producttype']
    search_fields=['tex']
    ordering=['id']
    list_per_page=10

@admin.register(news)
class newsadmin(admin.ModelAdmin):
    list_display=['title','post_time','text']

@admin.register(Product)
class newsadmin(admin.ModelAdmin):
    list_display=['name','price','image','description']

@admin.register(pic_display)
class newsadmin(admin.ModelAdmin):
    list_display=['section','ordering','image','introd']
    ordering=['section','ordering']
@admin.register(PersonCount)
class newsadmin(admin.ModelAdmin):
    list_display=['person_count']


from . import views
from django.urls import path,re_path,re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path("",views.home),
    path("order/",views.order_.as_view()),
    path("news/<int:detail_id>/",views.new_show),
    path("price/",views.price_show),  
]
if settings.DEBUG is False:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

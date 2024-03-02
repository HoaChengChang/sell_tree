import time
from .models import *


def timeit_middleware(get_response):
    
    def middleware(request):
        start = time.time()
        response = get_response(request)
        end = time.time()
        print("请求花费时间: {}秒".format(end - start))
        return response

    return middleware

def CountPerson(get_response):
    def middleware(request):
        # obj=PersonCount.objects.get_or_create(pk=1)
        # print(obj[0].person_count)
        # if obj:
        #     total=obj[0].person_count+1
        #     PersonCount.objects.filter(pk=1).update(person_count=total)
        # else:
        #     obj=PersonCount()
        #     obj.save()
            
        response = get_response(request)
        return response
    return middleware
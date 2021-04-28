from django.shortcuts import render,HttpResponse
import os

from django.views.decorators.csrf import csrf_exempt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


"""
django-admin startproject car
manage.py runserver 0.0.0.0:8000
"""


def main(request):
    context = {'content': "车牌识别"}
    return render(request, 'index.html',  context)


@csrf_exempt
def upload(request):
    try:
        my_file = request.FILES.get("licensePlate", None)
        if my_file:
            path = os.path.join(BASE_DIR, 'images')
            destination = open(os.path.join(path, my_file.name),
                               'wb+')
            for chunk in my_file.chunks():
                destination.write(chunk)
            destination.close()
    except Exception as e:
        return HttpResponse({'status': False, 'msg': u'错误：{}'.format(e)})
    return HttpResponse('ok')


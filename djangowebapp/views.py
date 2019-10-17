from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from datetime import datetime

import random


# Create your views here.
def index(request):
    # template = loader.get_template('test/index.html')

    current = datetime.now()

    context = {
        'current_date': current
    }

    # return HttpResponse("Hello World!")
    # return HttpResponse(template.render(context, request))
    return render(request, 'test/index.html', context)


def select(request):
    # message = '수 하나를 입력하세요.'
    # return HttpResponse(message)

    context = {
        'number': 4
    }

    return render(request, 'test/select.html', context)


def result(request):
    # message = '추첨 결과입니다.'
    # return HttpResponse(message)

    num = request.GET['number']

    context = {
        # 'num_arr': [1, 2, 3, 4, 5, 6]
        'num_arr': [num, 2, 3, 4, 5, 6]
    }

    return render(request, 'test/result.html', context)

from django.shortcuts import render
from django.http import HttpResponseRedirect

from djangomydb.models import Post

from .forms import PostForm


# Create your views here.
def list(request):
    context = {
        'items': Post.objects.all()
    }

    return render(request, 'test/list.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            # print(form)
            # 'form'에 입력한 내용을 저장,
            new_item = form.save()
        else:
            # 'form'에 입력한 내용을 웹페이지로 보여주기
            return HttpResponseRedirect('/mydb/list/')

    if request.method == 'GET':
        form = PostForm()

    context = {
        'form': form
    }

    return render(request, 'test/create.html', context)


def confirm(request):
    form = PostForm(request.POST)

    context = {
        'form': form
    }

    if form.is_valid():
        return render(request, 'test/confirm.html', context)
    else:
        return HttpResponseRedirect('/mydb/create/')

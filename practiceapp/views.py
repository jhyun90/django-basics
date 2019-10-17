from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.db.models import Count, Avg

from .models import Restaurant, Review
from .forms import RestaurantForm, ReviewForm, UpdateRestaurantForm


# Create your views here.
def list(request):
    # Count()의 인자 값인 'review'는 'models.py'에서 정의한 클래스 'Review'의 이름을 따라 장고 규칙 상 (with all lower case) 'review'라는 이름으로 선언된다.
    restaurants = Restaurant.objects.all().annotate(reviews_count=Count('review')).annotate(average_point=Avg('review__point'))
    paginator = Paginator(restaurants, 5)

    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        # 'restaurants': Restaurant.objects.all()
        'restaurants': items
    }

    return render(request, 'app/list.html', context)


def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)

        if form.is_valid():
            new_item = form.save()

        return HttpResponseRedirect('/practiceapp/list/')   # 링크 맨 앞에 '/' 빠뜨리지 않기

    else:
        form = RestaurantForm()

        context = {
            'form': form
        }

        return render(request, 'app/create.html', context)


def update(request):
    # 'primary key'를 포함한 요청을 통해 어떤 데이터의 정보를 업데이트 할 것인가를 결정 가능
    if request.method == 'POST' and 'id' in request.POST:
        # item = Restaurant.objects.get(pk=request.POST.get('id'))
        item = get_object_or_404(Restaurant, pk=request.POST.get('id'))
        password = request.POST.get('password', '')
        # form = RestaurantForm(request.POST, instance=item)
        form = UpdateRestaurantForm(request.POST, instance=item)

        if form.is_valid() and password == item.password:
            item = form.save()

        # return HttpResponseRedirect('/practiceapp/list/')

    # else:
    elif request.method == 'GET':
        # item = Restaurant.objects.get(pk=request.GET.get('id')) # app/update?id=2
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)

        context = {
            'form': form
        }

        return render(request, 'app/update.html', context)

    return HttpResponseRedirect('/practiceapp/list/')


def detail(request, id):
    # if 'id' in request.GET:
    if id is not None:
        # item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item = get_object_or_404(Restaurant, pk=id)
        reviews = Review.objects.filter(restaurant=item).all()

        return render(request, 'app/detail.html', context={'item': item, 'reviews': reviews})

    else:
        return HttpResponseRedirect('/practiceapp/list/')


def delete(request, id):
    # if 'id' in request.GET:
    #     item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
    #     item.delete()
    #
    # return HttpResponseRedirect('/practiceapp/list/')

    item = get_object_or_404(Restaurant, pk=id)

    if request.method == 'POST' and 'password' in request.POST:
        if item.password == request.POST.get('password') or item.password is None:
            item.delete()

            return redirect('list')

        else:
            return redirect('restaurant-detail', id=id)

    else:
        return render(request, 'app/delete.html', context={'item': item})


def review_create(request, restaurant_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            new_item = form.save()

        # 'view name' 연동을 기반으로, 'url'을 직접 입력/수정할 필요가 없음
        return redirect('restaurant-detail', id=restaurant_id)

    item = get_object_or_404(Restaurant, pk=restaurant_id)

    # 사용자가 입력할 평가의 대상이 될 식당을 설정하기 위한 작업
    form = ReviewForm(initial={'restaurant': item})

    return render(request, 'app/review_create.html', context={'form': form, 'item': item})


def review_delete(request, restaurant_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()

    return redirect('restaurant-detail', id=restaurant_id)


def review_list(request):
    reviews = Review.objects.all().select_related().order_by('-created_at')
    paginator = Paginator(reviews, 10)

    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'reviews': items
    }

    return render(request, 'app/review_list.html', context)

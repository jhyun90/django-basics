from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    image = models.CharField(max_length=500, default=None, null=True)
    password = models.CharField(max_length=20, default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    # 맛집에 대한 평가는 그 식당이 존재하는 경우에 한하여 가능하며,
    # 따라서, 평가를 남기거나 또는 다른 사람들의 평가를 보고자 한다면, 해당 맛집의 홈페이지를 방문(참조)해야 가능하고,
    # 이는 맛집에 대한 평가가 곧 해당 식당에 귀속된다고 할 수 있다.

    # 'Review' 클래스에서는 각 식당의 고유한 정보인 기본키('id')를 참조하는 '외래 키'를 선언하여,
    # 두 테이블(Restaruant, Review) 간의 관계를 참조 무결성을 기반으로 규정한다.
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    # restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING())

    # on_delete=models.CASCADE
    # 식당에 대한 정보가 삭제되는 경우, 해당 식당에 대해 작성된 평가도 함께 삭제되도록 설정

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

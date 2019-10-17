from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from practiceapp.models import Restaurant, Review

REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5)
)


class ReviewForm(ModelForm):
    class Meta:
        model = Review

        fields = ['point', 'comment', 'restaurant']

        labels = {
            'point': _('평점'),
            'comment': _('평가'),
        }

        help_texts = {
            'point': _('평점을 입력하세요'),
            'comment': _('평가를 입력하세요'),
        }

        widgets = {
            'restaurant': forms.HiddenInput(),
            'point': forms.Select(choices=REVIEW_POINT_CHOICES),
        }


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant

        fields = ['name', 'address', 'image', 'password']

        labels = {
            'name': _('이름'),
            'address': _('주소'),
            'image': _('이미지 url'),
            'password': _('게시물 비밀번호'),
        }

        help_texts = {
            'name': _('이름을 입력하세요'),
            'address': _('주소를 입력하세요'),
            'image': _('이미지 url을 입력하세요.'),
            'password': _('게시물 비밀번호를 입력하세요.'),
        }

        widgets = {
            'password': forms.PasswordInput()
        }

        error_messages = {
            'name': {
                'max_length': _('입력이 30자 이하로 제한되어 있습니다.')
            },

            'image': {
                'max_length': _('입력이 500자 이하로 제한되어 있습니다.')
            },

            'password': {
                'max_length': _('입력이 20자 이하로 제한되어 있습니다.')
            },
        }


class UpdateRestaurantForm(RestaurantForm):
    class Meta:
        model = Restaurant
        exclude = ['password']

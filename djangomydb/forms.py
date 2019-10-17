from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# 'models.py' 생성 후 import 작업
from djangomydb.models import Post


# class PostForm(forms.Form):
#     title = forms.CharField(label='제목', max_length=200)
#     content = forms.CharField(label='내용', widget=forms.Textarea)


class PostForm(ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'content']

        labels = {
            'title': _('제목'),
            'content': _('내용'),
        }

        help_texts = {
            'title': _('제목을 입력하세요.'),
            'content': _('내용을 입력하세요.'),
        }

        error_messages = {
            'name': {
                'max_length': _('제목이 정해진 길이를 초과하였습니다. 다시 입력하세요.'),
            }
        }

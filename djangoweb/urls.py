"""djangoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from djangowebapp import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('webapp/', include('djangowebapp.urls')),
    path('mydb/', include('djangomydb.urls')),
    path('practiceapp/', include('practiceapp.urls')),
    path('admin/', admin.site.urls),
]

# 1. web/urls.py -> path 설정: webapp/, mydb
# 2. webapp/urls.py -> path 설정: select/, result/
# 3. mydb/urls.py -> path 설정: path('list/', views.list, name="list"), path('create/', views.create, name="create"),
# 3-1. views.py -> def list(), def create()
# 3-1-1. def list() -> return render(request, 'test/list.html', context)
# 3-1-2. def create() -> return render(request, 'test/create.html', context)
# 3-3. test/create.html, test/list.html 생성
# 3-4. context -> forms.py 생성 (웹페이지 화면에 표시할 테이블, 레이블 등을 정의);
#     'test/create.html' 내부에 'from .forms import PostForm' + 'from djangomydb.models import Post'
# 3-5. models.py -> 'forms.py' 생성을 통해 웹페이지 화면에 표시할 데이터 정보들에 대한 자료형 정의;
#     'forms.py' 내부에 'from djangomydb.models import Post'

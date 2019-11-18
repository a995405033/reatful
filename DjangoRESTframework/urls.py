"""DjangoRESTframework URL Configuration

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
from DjangoRESTframework import views
from django.conf.urls import url, include

from rest_framework import routers  # 导入rest_framework的路由模块
from sqLite3.rest_views import BookViewSet  # 展示序列化视图函数
from sqLite3.rest_views import AuthorViewSet  # 展示序列化视图函数
from DjangoRESTframework import views

router = routers.DefaultRouter()
router.register(r'Book', BookViewSet)  # 配置URL，配置展示的表名
router.register(r'Author', AuthorViewSet)  # 配置URL，配置展示的表名



urlpatterns = [

    url('api/', include(router.urls)),  # 配置路由
    url('admin/', admin.site.urls),
    url("index/$", views.index),
    url(r'api/v1/auth/$',views.AuthView.as_view()),

]

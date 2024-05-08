"""
URL configuration for site1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from django.views.static import serve
import helloWorld.views
import helloWorld.struct.student_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', helloWorld.views.index),
    # 配置媒体文件的路由地址
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    path('plant/<str:name>', helloWorld.views.plant),
    path('redirectTo', RedirectView.as_view(url="index/")),

    # 命名空间 namespace
    path('user/', include(('user.urls', 'user'), 'user')),
    path('order/', include(('order.urls', 'order'), 'order')),

    path('get', helloWorld.views.get_test),
    path('post', helloWorld.views.post_test),

    path('tologin/', helloWorld.views.login_default),
    path('login', helloWorld.views.login),
    path('login_check', helloWorld.views.login_check),

    path('toUpload/', helloWorld.views.to_upload),
    path('upload', helloWorld.views.upload),

    path('student/list', helloWorld.views.Student.as_view()),
    path('student/<int:pk>', helloWorld.struct.student_list.StudentDetail.as_view())
]

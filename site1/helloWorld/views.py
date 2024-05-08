import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from helloWorld.models import StudentInfo


# Create your views here.
def index(request):
    return render(request, 'http.html')
    # print("The page request is being processing")
    # return render(request, 'index2.html')


def plant(request, name):
    # 可根据参数选择返回参数
    if not name or name == '0':
        return redirect("/static/error.html")
    else:
        return HttpResponse("name is {} plant".format(name))


def get_test(request):
    print("The page request is being processing")
    print(request.method)  # 请求方式
    # 常用属性
    print(request.content_type)
    print(request.content_params)
    print(request.COOKIES)
    print(request.scheme)
    print(request.META)
    # 常用方法
    print(request.is_secure())
    print(request.get_host())
    print(request.get_full_path())

    print(request.GET)
    print(request.GET.get("name"))
    print(request.GET.get("pwd"))
    print(request.GET.get("None", "default"))

    return HttpResponse("http get ok")


def post_test(request):
    """
    post请求测试
    :param request:
    :return:
    """
    print(request.method)
    print(request.POST.get("name"))
    print(request.POST.get("pwd"))
    print(request.POST.get("default", "12121"))
    print(request.COOKIES)
    return HttpResponse("http post ok")


def to_login(request):
    """
    跳轉登錄頁面
    :param request:
    :return:
    """
    return render(request, 'login.html')


def login(request):
    """
    登錄
    :param request:
    :return:
    """
    user_name = request.POST.get("user_name")
    pwd = request.POST.get("pwd")
    if user_name == "xunzf" and pwd == "123456":
        request.session["currentUserName"] = user_name  # session中存一個用戶名
        print("session獲取：", request.session["currentUserName"])
        response = render(request, "main.html")
        response.set_cookie("remember_me", True)  # 設置cookies
        return response
    else:
        context_value = {"error_info": "用戶名或者密碼錯誤"}
        return render(request, 'login.html', context=context_value)


def login_check(request):
    user_name = request.POST.get("user_name")
    pwd = request.POST.get("pwd")
    remember_me = request.POST.get("remember_me")
    if user_name == "xunzf" and pwd == "123456":
        request.session["currentUserName"] = user_name
        response = render(request, "main.html")
        if remember_me == 'on':
            response.set_cookie("user_name", user_name, max_age=100)
            response.set_cookie("pwd", pwd, max_age=100)
            return response
        else:
            return render(request, "main.html")


def login_default(request):
    user_name = ""
    pwd = ""
    if "user_name" in request.COOKIES and "pwd" in request.COOKIES:
        user_name = request.COOKIES["user_name"]
        pwd = request.COOKIES["pwd"]
    else:
        pass
    return render(request, 'login_check.html', {"user_name": user_name, "pwd": pwd})


def to_upload(request):
    """
    调整文件上传页面
    :param request:
    :return:
    """
    return render(request, 'upload.html')


def upload(request):
    """
    文件上传处理
    :param request:
    :return:
    """
    # 获取上传的文件，没有的话，返回None
    my_file = request.FILES.get("myfile", None)
    if my_file:
        path = os.path.join(os.path.abspath('.'), 'myfile')
        f = open(os.path.join(".\\helloWorld\\myfile", my_file.name), "wb+")
        # 分块写入
        for chunk in my_file.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse("文件上传成功")
    else:
        return HttpResponse("没发现文件")


class Student(ListView):
    # 设置模板文件
    template_name = 'student/list.html'
    # 设置模型外的数据
    extra_context = {'title': 'Student List Info'}
    # 查询结果集
    queryset = StudentInfo.objects.all()
    # 煤业展示5条数据
    paginate_by = 5
    # 设置上下文对象名称
    context_object_name = 'student_info'

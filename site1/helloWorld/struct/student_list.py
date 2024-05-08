from django.views.generic import ListView, DetailView

from helloWorld.models import StudentInfo


class Student(ListView):
    # 设置模板文件
    template_name = 'student/list.html'
    # 设置模型外的数据
    extra_context = {'title': 'Student List Info'}
    # 查询结果集
    queryset = StudentInfo.objects.all()
    # 设置上下文对象名称
    context_object_name = 'student_info'


class StudentDetail(DetailView):
    # 设置模板文件
    template_name = 'student/detail.html'
    # 设置模型外的数据
    extra_context = {'title': 'Student Detail'}
    # 设置查询模型
    model = StudentInfo
    # 设置上下文对象名称
    context_object_name = 'student_detail'

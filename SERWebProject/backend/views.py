from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import RegisterForm, UserInfoForm
from .models import Project
from django.contrib import auth
from django.core import serializers
import json


# from oauthlib.oauth2 import LegacyApplicationClient
# from requests_oauthlib import OAuth2Session

# Create your views here.
def hello(request):
    return HttpResponse("Hello!")


def projreg(request):
    latest_project_list = Project.objects.order_by('-pub_date')[:5]
    context = {'latest_project_list': latest_project_list}
    return render(request, 'backend/projreg.html', context)


def detail(request, project_id):
    return HttpResponse("You're looking at question %s." % project_id)


def results(request, project_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % project_id)


def vote(request, project_id):
    return HttpResponse("You're voting on question %s." % project_id)


def register(request):
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'GET':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、client_ID、client_secret、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.GET)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            # 注册成功，跳转回首页
            return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'backend/register.html', context={'form': form})


def login(request):
    username = request.GET['username']
    password = request.GET['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return JsonResponse({'status': 0})
    else:
        # Show an error page
        return JsonResponse({'status': 1})


def project_list_display(request):
    response = {}
    if request.method == 'GET':
        latest_project_list = Project.objects.order_by('-project_hot')[:20]
        response['list'] = json.loads(serializers.serialize("json", latest_project_list))
        response['msg'] = 'success'
        response['error_num'] = 0

    return JsonResponse(response)


def project_card_display(request):
    response = {}
    if request.method == 'GET':
        hottest_project_list = Project.objects.order_by('-project_hot')[:3]
        response['list'] = json.loads(serializers.serialize("json", hottest_project_list))
        response['msg'] = 'success'
        response['error_num'] = 0

    return JsonResponse(response)


def user_info_submit(request):
    if request.method == 'GET':
        form = UserInfoForm(request.GET)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = RegisterForm()

    return render(request, 'backend/register.html', context={'form': form})

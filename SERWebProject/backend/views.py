from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.template import loader
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import RegisterForm, UserInfoForm
from .models import Project, User, ProjectRegisterRelationship, UserInfo, Group, Membership
from django.contrib import auth
from django.core import serializers
from django.utils import timezone
import json


# from oauthlib.oauth2 import LegacyApplicationClient
# from requests_oauthlib import OAuth2Session

# Create your views here.
@csrf_exempt
def register(request):
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password1）、确认密码（password2）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            new_user = form.save()
            # 用户认证后创建未激活用户信息页
            new_user.userinfo_set.create(user=new_user, name=new_user.username + ' 未激活用户信息')
            # 注册成功，跳转回首页
            return HttpResponse('register success!')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'backend/register.html', context={'form': form})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # return user_info, including user_id(pk)
            user_info = User.objects.filter(username=username)
            response = {'list': json.loads(serializers.serialize("json", user_info)),
                        'msg': 'success',
                        'status': 0}
            # Redirect to a success page.
            return JsonResponse(response)
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


@csrf_exempt
def user_info_submit(request, user_id):
    if request.method == 'POST':
        # 用户
        user = User.objects.get(pk=user_id)
        # 用户信息表
        user_info = UserInfo.objects.get(user=user)
        # 更新用户信息表
        form = UserInfoForm(request.POST, instance=user_info)

        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.save()
            user.submit_info = True
            user.save()

            return HttpResponse('submit user info success')

    else:
        form = UserInfoForm()

    return render(request, 'backend/register.html', context={'form': form})


def user_info_request(request, user_id):
    response = {}
    if request.method == 'GET':
        try:
            user = User.objects.filter(pk=user_id)
            user_info = UserInfo.objects.filter(user=user)
            response['list'] = json.loads(serializers.serialize("json", user_info))
            response['msg'] = 'success'
            response['error_num'] = 0
        except:
            raise Http404("User does not exist")

    return JsonResponse(response)


def project_info_request(request, project_id):
    response = {}
    if request.method == 'GET':
        try:
            project_info = Project.objects.filter(pk=project_id)
            response['list'] = json.loads(serializers.serialize("json", project_info))
            response['msg'] = 'success'
            response['error_num'] = 0
        except:
            raise Http404("Project does not exist")

    return JsonResponse(response)


@csrf_exempt
def project_register(request, user_id, project_id):
    if request.method == 'POST':
        try:
            user = User.objects.get(pk=user_id)
            user_info = UserInfo.objects.get(user=user)
            project = Project.objects.get(pk=project_id)
            if project.was_below_max_reg():
                project_register_form = ProjectRegisterRelationship(user=user, user_info=user_info,
                                                                    register_name = user_info.name,
                                                                    student_id=user_info.student_id,
                                                                    project=project,
                                                                    registed_project_name=project.project_name,
                                                                    register_datetime=timezone.now())
                project_register_form.save()
                project.project_hot = project.project_hot + 1
                project.save()
                return HttpResponse("Success!")
            else:
                return HttpResponse("This project already reach its register max")
        except:
            raise Http404("Register error!")

    return render(request, 'backend/register.html', context={'form': ProjectRegisterRelationship})


def project_register_relationship_request(request, user_id):
    response = {}
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=user_id)
            latest_project_register_relationship_list = ProjectRegisterRelationship.objects.filter(user=user).order_by('-register_datetime')
            response['list'] = json.loads(serializers.serialize("json", latest_project_register_relationship_list))
            response['msg'] = 'success'
            response['error_num'] = 0
            return JsonResponse(response)
        except:
            raise Http404('请求用户已报名项目列表失败！')
    else:
        raise Http404('请求用户已报名项目列表失败！')


def project_grade_request(request, project_id):
    response = {}
    if request.method == 'GET':
        try:
            project = Project.objects.get(pk=project_id)
            try:
                project_grade = ProjectRegisterRelationship.objects.filter(project=project)
                response['list'] = json.loads(serializers.serialize("json", project_grade))
                response['msg'] = 'success'
                response['error_num'] = 0
                return JsonResponse(response)
            except:
                return HttpResponse('project grade does not exist')
        except:
            return HttpResponse('project does not exist!')
    else:
        raise Http404('request project grade error!')


@csrf_exempt
def add_group(request, user_id, project_id):
    if request.method == 'POST':
        try:
            group_name = request.POST['group_name']
            project = Project.objects.get(pk=project_id)
            team_leader = User.objects.get(pk=user_id)
            team_leader_info = UserInfo.objects.get(user=team_leader)
            team_min_reg = project.team_min_reg
            team_max_reg = project.team_max_reg
            new_group = Group(group_name=group_name, project=project, team_creator=team_leader,
                              team_creator_info=team_leader_info, team_min_reg=team_min_reg, team_max_reg=team_max_reg)
            if project.was_below_max_reg:
                new_group.save()
                project.project_hot = project.project_hot + 1
                project.save()
                return HttpResponse('success!')
            else:
                return HttpResponse('This project already reach its register team cap')
        except:
            return HttpResponse('error!')
    else:
        return HttpResponse('Please check request method!')


@csrf_exempt
def add_teammate(request, user_id, project_id):
    if request.method == 'POST':
        name = request.POST['name']
        try:
            team_creator = User.objects.get(pk=user_id)
            project = Project.objects.get(pk=project_id)
            group = Group.objects.get(team_creator=team_creator, project=project)
            team_creator_info = UserInfo.objects.get(user=team_creator)
            new_teammate_info = UserInfo.objects.get(name=name)
            if new_teammate_info is not None and group.if_below_team_max_reg:
                new_teammate = User.objects.get(belong_to=new_teammate_info)
                new_teammate_addon = Membership(project=project, group=group, team_leader=team_creator,
                                                team_leader_info=team_creator_info,
                                                teammate=new_teammate, teammate_info=new_teammate_info)
                new_teammate_addon.save()
                group.teammate_num = group.teammate_num + 1
                group.save()
                return JsonResponse({'status': 0, 'msg': '添加成功！'})
        except:
            return JsonResponse({'status': 1, 'msg': '用户不存在或未激活！'})
    else:
        return HttpResponse('add teammate request error!')


@csrf_exempt
def set_teammate_confirm(request, user_id, project_id):
    if request.method == 'POST':
        try:
            team_creator = User.objects.get(pk=user_id)
            project = Project.objects.get(pk=project_id)
            group = Group.objects.get(team_creator=team_creator, project=project)
            group.if_teammate_finally_confirm = True
            group.save()
            return HttpResponse('confirm!')
        except:
            return HttpResponse('no such team!')
    else:
        return HttpResponse('please check request method!')






from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Project


# Create your views here.
def hello(request):
    return HttpResponse("Hello world! This is SERWeb project!")


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

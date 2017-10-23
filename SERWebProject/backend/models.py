import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=30)  # 项目名称
    project_text = models.CharField(max_length=200)  # 项目描述
    pub_date = models.DateTimeField('date published')  # 发布时间

    def __str__(self):
        return self.project_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=10)
    votes = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class User(AbstractUser):
    client_ID = models.CharField(max_length=30)
    client_secret = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        pass

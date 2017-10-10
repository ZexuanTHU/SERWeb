from django.db import models


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=30)  # 项目名称
    project_text = models.CharField(max_length=200)  # 项目描述
    pub_date = models.DateTimeField('date published')  # 发布时间

    def __str__(self):
        return self.project_name


class Choice(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=10)
    votes = models.BooleanField(default=False)

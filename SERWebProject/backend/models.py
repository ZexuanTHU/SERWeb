import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=30)  # 项目名称
    project_text = models.CharField(max_length=200)  # 项目描述
    pub_date = models.DateTimeField('date published')  # 发布时间
    ddl_date = models.DateTimeField('registration deadline')  # 发布时间
    max_reg = models.IntegerField(default=100)
    contact_name = models.CharField(max_length=30, default='郭志芃')
    contact_tel = models.CharField(max_length=30, default='18813040000')
    project_hot = models.IntegerField(default=0)
    group_project = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_below_max_reg(self):
        if self.max_reg - self.project_hot >= 0:
            return True
        else:
            return False

    def show_project_hot(self):
        return self.project_hot


class Choice(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=10)
    votes = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class User(AbstractUser):
    # email = models.EmailField()
    MALE = 'M'
    FEMALE = 'F'
    GENDER = (
        (MALE, '男'),
        (FEMALE, '女')
    )

    BACHELOR = 'BS'
    MASTER = 'MS'
    DOCTOR = 'PhD'
    READING_DEGREE = (
        (BACHELOR, '本科生'),
        (MASTER, '硕士'),
        (DOCTOR, '博士')
    )

    CLOTHES_SIZE = {
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL')
    }

    name = models.CharField('姓名', max_length=10)
    student_id = models.CharField('学号', max_length=10)
    id_card = models.CharField('身份证号', max_length=18)
    gender = models.CharField('性别', choices=GENDER, max_length=1)
    birth_date = models.TimeField('出生日期', default=timezone.now())
    reading_degree = models.CharField('攻读学位', choices=READING_DEGREE, max_length=3)
    faculty = models.CharField('院系', max_length=20)
    class_id = models.CharField('班级', max_length=10)
    clothes_size = models.CharField('衣服尺寸', choices=CLOTHES_SIZE, max_length=2)
    email = models.EmailField()
    cellphone_num = models.CharField('手机号码', max_length=11)
    dormitory = models.CharField('寝室号码', max_length=20)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        pass

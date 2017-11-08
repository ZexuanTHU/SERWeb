import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # email = models.EmailField()
    submit_info = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        pass


class UserInfo(models.Model):
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

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField('姓名', max_length=10)
    student_id = models.CharField('学号', max_length=10)
    id_card = models.CharField('身份证号', max_length=18)
    gender = models.CharField('性别', choices=GENDER, max_length=1)
    birth_date = models.DateField('出生日期', default=timezone.now())
    reading_degree = models.CharField('攻读学位', choices=READING_DEGREE, max_length=3)
    faculty = models.CharField('院系', max_length=20)
    class_id = models.CharField('班级', max_length=10)
    clothes_size = models.CharField('衣服尺寸', choices=CLOTHES_SIZE, max_length=2)
    email = models.EmailField()
    cellphone_num = models.CharField('手机号码', max_length=11)
    dormitory = models.CharField('寝室号码', max_length=20)

    def __str__(self):
        return self.name + '(' + self.user.username + ')' + ' 个人信息表'

    class Meta:
        verbose_name = '用户信息表 UserInfo'
        verbose_name_plural = '用户信息表 UserInfo'


class Project(models.Model):
    project_name = models.CharField('项目名称', max_length=30)  # 项目名称
    project_text = models.CharField('项目描述', max_length=200)  # 项目描述
    pub_date = models.DateTimeField('发布时间', default=timezone.now())  # 发布时间
    ddl_date = models.DateTimeField('报名截止日期', default=timezone.now())  # 发布时间
    match_data_time = models.DateTimeField('比赛时间', default=timezone.now())
    match_venue = models.CharField('比赛地点', max_length=30, default='清华大学')
    contact_name = models.CharField('紧急联系人姓名', max_length=30, default='郭志芃')
    contact_tel = models.CharField('紧急联系人电话', max_length=30, default='18813040000')
    group_project = models.BooleanField('是否为团体项目', default=False)
    # 个人项目字段
    min_reg = models.IntegerField('报名人数/队伍数下限', default=0)
    max_reg = models.IntegerField('报名人数/队伍数上限', default=100)
    project_hot = models.IntegerField('当前报名人数/队伍数', default=0)
    team_min_reg = models.IntegerField('队伍人数下限', default=0)
    team_max_reg = models.IntegerField('队伍人数上限', default=0)
    registered_user = models.ManyToManyField(User, through='ProjectRegisterRelationship')
    registered_user_info = models.ManyToManyField(UserInfo, through='ProjectRegisterRelationship')

    class Meta:
        verbose_name = '项目 Project'
        verbose_name_plural = '项目 Project'

    def __str__(self):
        return self.project_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_below_max_reg(self):
        if self.max_reg - self.project_hot > 0:
            return True
        else:
            return False

    def show_project_hot(self):
        return self.project_hot


class ProjectRegisterRelationship(models.Model):
    PENDING = 'PE'
    APPROVED = 'AP'
    REJECTED = 'RE'
    APPROVAL_STATUS = (
        (PENDING, '审核中'),
        (APPROVED, '已通过'),
        (REJECTED, '未通过')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    register_name = models.CharField('选手姓名', max_length=10, default='选手')
    student_id = models.CharField('学号', max_length=10, default='2014000000')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    registered_project_name = models.CharField('项目名称', max_length=20, default='项目')
    register_datetime = models.DateTimeField('报名时间')
    approval_status = models.CharField('报名审核状态', max_length=10, choices=APPROVAL_STATUS, default=PENDING)
    grade = models.CharField('比赛成绩', max_length=100, default='完赛')
    if_finished = models.BooleanField('比赛已结束', default=False)

    def __str__(self):
        return self.approval_status + ' ' + self.project.project_name + ' ' + self.user_info.name + '(' + self.user.username + ')'

    class Meta:
        verbose_name = '项目报名表 ProjectRegisterRelationship'
        verbose_name_plural = '项目报名表 ProjectRegisterRelationship'


class Group(models.Model):
    group_name = models.CharField(max_length=128, default='队伍')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    team_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_creator')
    members = models.ManyToManyField(User, through='Membership', through_fields=('group', 'teammate'))

    def __str__(self):
        return self.project.project_name + ' ' + self.group_name + ' ' + self.team_creator.username

    class Meta:
        verbose_name = '团队 Group'
        verbose_name_plural = '团队 Group'


class Membership(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    group = models.ForeignKey(Group)
    team_leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_leader_created_this_team")
    team_leader_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="team_leader_info")
    teammate = models.ForeignKey(User, on_delete=models.CASCADE)
    teammate_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.project_name + ' ' + self.group.group_name + ' ' + \
               self.team_leader_info.name + ' ' + self.teammate_info.name

    class Meta:
        verbose_name = '团队报名表 Membership'
        verbose_name_plural = '团队报名表 Membership'

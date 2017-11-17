import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
PENDING = 'PE'
APPROVED = 'AP'
REJECTED = 'RE'
APPROVAL_STATUS = (
    (PENDING, '审核中'),
    (APPROVED, '已通过'),
    (REJECTED, '未通过')
)

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


class User(AbstractUser):
    # email = models.EmailField()
    submit_info = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        pass


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='belong_to')
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
    # 个人项目字段
    min_reg = models.IntegerField('报名人数/队伍数下限', default=0)
    max_reg = models.IntegerField('报名人数/队伍数上限', default=100)
    project_hot = models.IntegerField('当前报名人数/队伍数', default=0)
    registered_user = models.ManyToManyField(User, through='ProjectRegisterRelationship')
    registered_user_info = models.ManyToManyField(UserInfo, through='ProjectRegisterRelationship')
    # 团体项目字段
    group_project = models.BooleanField('是否为团体项目', default=False)
    team_min_reg = models.IntegerField('队伍人数下限', default=1)
    team_max_reg = models.IntegerField('队伍人数上限', default=5)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    register_name = models.CharField('选手姓名', max_length=10, default='选手')
    student_id = models.CharField('学号', max_length=10, default='2014000000')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    registered_project_name = models.CharField('项目名称', max_length=20, default='项目')
    register_datetime = models.DateTimeField('报名时间', default=timezone.now())
    approval_status = models.CharField('报名审核状态', max_length=10, choices=APPROVAL_STATUS, default=PENDING)
    rank = models.IntegerField('排名', default=0)
    grade = models.CharField('比赛成绩', max_length=100, default='比赛尚未结束')
    if_finished = models.BooleanField('比赛已结束', default=False)
    if_group_project = models.BooleanField('是否为团队项目', default=False)

    def __str__(self):
        return self.approval_status + ' ' + self.project.project_name + ' ' + self.user_info.name + '(' + self.user.username + ')'

    def delete(self, using=None, keep_parents=False):
        self.project.project_hot = self.project.project_hot - 1
        self.project.save()
        super(ProjectRegisterRelationship, self).delete()

    def if_approval_status_still_pending(self):
        if self.approval_status == PENDING:
            return True
        else:
            return False

    class Meta:
        verbose_name = '项目报名表 ProjectRegisterRelationship'
        verbose_name_plural = '项目报名表 ProjectRegisterRelationship'


class Group(models.Model):
    group_name = models.CharField(max_length=128, default='队伍')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    team_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_creator')
    team_creator_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='team_creator_info')
    team_creator_name = models.CharField("队长姓名", max_length=10, default='队长')
    team_min_reg = models.IntegerField('队伍人数下限', default=1)
    team_max_reg = models.IntegerField('队伍人数上限', default=0)
    teammate_num = models.IntegerField('队伍当前人数', default=1)
    members = models.ManyToManyField(User, through='Membership', through_fields=('group', 'teammate'))
    register_datetime = models.DateTimeField('报名时间', default=timezone.now())
    approval_status = models.CharField('报名审核状态', max_length=10, choices=APPROVAL_STATUS, default=PENDING)
    rank = models.IntegerField('排名', default=0)
    grade = models.CharField('比赛成绩', max_length=100, default='比赛尚未结束')
    if_finished = models.BooleanField('比赛已结束', default=False)
    if_teammate_finally_confirm = models.BooleanField('已提交队员名单', default=False)
    if_group_project = models.BooleanField('是否团队项目', default=True)

    def __str__(self):
        return self.project.project_name + ' ' + self.group_name + ' ' + self.team_creator_info.name + '(' + \
               self.team_creator.username + ')'

    def if_exceed_team_min_reg(self):
        if self.team_min_reg - self.teammate_num < 0:
            return True
        else:
            return False

    def if_below_team_max_reg(self):
        if self.team_max_reg - self.teammate_num > 0:
            return True
        else:
            return False

    def delete(self, using=None, keep_parents=False):
        self.project.project_hot = self.project.project_hot - 1
        self.project.save()
        super(Group, self).delete()

    def if_approval_status_still_pending(self):
        if self.approval_status == PENDING:
            return True
        else:
            return False

    class Meta:
        verbose_name = '团队 Group'
        verbose_name_plural = '团队 Group'


class Membership(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    group = models.ForeignKey(Group)
    group_name = models.CharField("队名", max_length=10, default='队伍')
    team_leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_leader_created_this_team")
    team_leader_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="team_leader_info")
    team_leader_name = models.CharField("队长姓名", max_length=10, default='队长')
    teammate = models.ForeignKey(User, on_delete=models.CASCADE)
    teammate_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    teammate_name = models.CharField("队员姓名", max_length=10, default='队员')
    register_datetime = models.DateTimeField('报名时间', default=timezone.now())
    rank = models.IntegerField('排名', default=0)
    grade = models.CharField('比赛成绩', max_length=100, default='比赛尚未结束')
    if_group_project = models.BooleanField('是否团队项目', default=True)

    def __str__(self):
        return self.project.project_name + ' ' + self.group.group_name + ' ' + \
               self.team_leader_info.name + '(' + self.team_leader.username + ')' + ' ' + self.teammate_info.name + \
               '(' + self.teammate.username + ')'

    def delete(self, using=None, keep_parents=False):
        self.group.teammate_num = self.group.teammate_num - 1
        self.group.save()
        super(Membership, self).delete()

    class Meta:
        verbose_name = '团队报名表 Membership'
        verbose_name_plural = '团队报名表 Membership'


class Carousel(models.Model):
    carousel_mark = models.CharField('轮播图题注', max_length=20, default='轮播图题注')
    carousel_image = models.ImageField(upload_to='')
    carousel_upload_time = models.DateTimeField('上传时间', default=timezone.now())
    if_carousel_active = models.BooleanField('是否激活', default=False)

    def __str__(self):
        return self.carousel_mark

    class Meta:
        verbose_name = '轮播图 Carousel'
        verbose_name_plural = '轮播图 Carousel'


class HallOfFame(models.Model):
    HOF_name = models.CharField('名人堂姓名', max_length=20, default='名人堂')
    HOF_gender = models.CharField('性别', choices=GENDER, max_length=1)
    HOF_selected_year = models.CharField('入选年份', max_length=4, default='2018')
    HOF_class_id = models.CharField('班级', default='计XX', max_length=5)
    HOF_introduction = models.TextField('个人简介', default='请输入个人简介(500字以内)', max_length=500)
    HOF_honor = models.TextField('个人荣誉', default='请输入个人荣誉(500字以内)', max_length=500)
    HOF_image = models.ImageField(upload_to='HallOfFame')
    HOF_upload_time = models.DateTimeField('上传时间', default=timezone.now())
    if_HOF_active = models.BooleanField('是否激活', default=False)

    def __str__(self):
        return self.HOF_name + ' ' + self.HOF_selected_year

    class Meta:
        verbose_name = '名人堂 Hall of Fame'
        verbose_name_plural = '名人堂 Hall of Fame'


class SchoolTeam(models.Model):
    school_team_name = models.CharField('名称', max_length=20, default='如：计算机男篮')
    school_team_gender = models.CharField('性别', choices=GENDER, max_length=1)
    school_team_introduction = models.TextField('队伍简介', default='请输入队伍简介(500字以内)', max_length=500)
    school_team_honor = models.TextField('队伍成员', default='请输入队伍成员(500字以内)', max_length=500)
    school_team_image = models.ImageField(upload_to='SchoolTeam')
    school_team_upload_time = models.DateTimeField('上传时间', default=timezone.now())
    if_school_team_active = models.BooleanField('是否激活', default=False)

    def __str__(self):
        return self.school_team_name

    class Meta:
        verbose_name = '院队 School Team'
        verbose_name_plural = '院队 School Team'

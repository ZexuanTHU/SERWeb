from django.contrib import admin
from .models import Project, User, ProjectRegisterRelationship, UserInfo, Group, Membership

# Register your models here.

admin.site.register(Project)
admin.site.register(User)
admin.site.register(UserInfo)
admin.site.register(ProjectRegisterRelationship)
admin.site.register(Group)
admin.site.register(Membership)


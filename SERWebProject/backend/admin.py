from django.contrib import admin
from .models import Project, User, ProjectRegisterRelationship, UserInfo, Group, Membership, Carousel, HallOfFame

admin.AdminSite.site_header = '清华大学计算机系体育赛事报名系统'
admin.AdminSite.site_title = 'SERWEb'


# Register your models here.

def delete_selected_project_register_relationship(modeladmin, request, queryset):
    for project in queryset:
        project.delete()
    delete_selected_project_register_relationship.short_description = "删除选中的条目"


class ProjectAdmin(admin.ModelAdmin):
    actions = ['delete_selected']


class UserAdmin(admin.ModelAdmin):
    actions = ['delete_selected']


class UserInfoAdmin(admin.ModelAdmin):
    actions = ['delete_selected']


class ProjectRegisterRelationshipAdmin(admin.ModelAdmin):
    actions = [delete_selected_project_register_relationship]


class GroupAdmin(admin.ModelAdmin):
    actions = [delete_selected_project_register_relationship]


class MembershipAdmin(admin.ModelAdmin):
    actions = [delete_selected_project_register_relationship]


class CarouselAdmin(admin.ModelAdmin):
    actions = ['delete_selected']


class HallOfFameAdmin(admin.ModelAdmin):
    actions = ['delete_selected']


admin.site.disable_action('delete_selected')
admin.site.register(Project, ProjectAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(ProjectRegisterRelationship, ProjectRegisterRelationshipAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(HallOfFame, HallOfFameAdmin)
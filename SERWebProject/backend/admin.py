from django.contrib import admin
from .models import Project, Choice, User

# Register your models here.

admin.site.register(Project)
admin.site.register(Choice)
admin.site.register(User)

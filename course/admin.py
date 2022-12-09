from django.contrib import admin
from course.models import course
from course.models import Join
# Register your models here.

admin.site.register(course)
admin.site.register(Join)
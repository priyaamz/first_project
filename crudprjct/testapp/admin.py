from django.contrib import admin
from testapp.models import employee

# Register your models here.
class EmployeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eadd']
admin.site.register(employee,EmployeAdmin)

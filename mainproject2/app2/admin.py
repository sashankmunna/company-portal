from django.contrib import admin
from app2.models import Employee,News,Calendar
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	list_display=['EmpName','EmpID','Designation','SalaryPackage','Department','Experience']
admin.site.register(Employee,EmployeeAdmin)

class NewsAdmin(admin.ModelAdmin):
	list_display=['occation']
admin.site.register(News,NewsAdmin)

class CalendarAdmin(admin.ModelAdmin):
	list_display = ['Date','Occation']
admin.site.register(Calendar, CalendarAdmin)
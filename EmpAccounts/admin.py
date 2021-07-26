from django.contrib import admin
from .models import *

admin.site.site_header = 'Employee Management Operator System'
admin.site.site_title = 'EMOS'
admin.site.index_title = 'Welcome to EMS Portal'

class EmpAdmin(admin.ModelAdmin):
    list_display= ('Name','Email','Department','apporoved_Status')
    search_fields = ('Name',)
    list_editable = ('apporoved_Status',)


admin.site.register(ApprovedEmp)
admin.site.register(EmpData,EmpAdmin)
admin.site.register(WorkingDay)
admin.site.register(AttendanceData)
admin.site.register(WorkDonePerDay)



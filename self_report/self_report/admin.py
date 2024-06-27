from django.contrib import admin
from .models import AttitudeForm, AttitudeModel, AbilityForm, AbilityModel, AchievementForm, AchievementModel, ScheduleForm, ScheduleModel, ReportModel, ReportForm
# Register your models here.

admin.site.register(AttitudeModel)
admin.site.register(AbilityModel)
admin.site.register(AchievementModel)
admin.site.register(ScheduleModel)
admin.site.register(ReportModel)
from django import forms
from accounts.models import User
from .models import AttitudeForm, AbilityForm, AchievementForm, ScheduleForm, ReportForm, ReportModel, ReportETCModel, ReportETCForm

class AttitudeForm(forms.Form):
    email = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    department = forms.CharField(max_length=200)
    team = forms.CharField(max_length=200)
    level = forms.CharField(max_length=200)
    attitude_01_01 = forms.CharField(max_length=200)
    attitude_01_02 = forms.CharField(max_length=200)
    attitude_02_01 = forms.CharField(max_length=200)
    attitude_02_02 = forms.CharField(max_length=200)
    attitude_02_03 = forms.CharField(max_length=200)
    attitude_02_04 = forms.CharField(max_length=200)
    attitude_03_01 = forms.CharField(max_length=200)
    attitude_03_02 = forms.CharField(max_length=200)
    attitude_03_03 = forms.CharField(max_length=200)
    attitude_04_01 = forms.CharField(max_length=200)
    attitude_04_02 = forms.CharField(max_length=200)
    attitude_04_03 = forms.CharField(max_length=200)
    attitude_04_04 = forms.CharField(max_length=200)
    attitude_05_01 = forms.CharField(max_length=200)
    attitude_05_02 = forms.CharField(max_length=200)
    post_id = forms.CharField(max_length=200)
    
    class Meta:
        model = AttitudeForm
        fields = ['mail', 'name', 'department', 'team', 'level', 'attitude_01_01', 'attitude_01_02', 'attitude_02_01', 'attitude_02_02', 'attitude_02_03', 'attitude_02_04', 'attitude_03_01', 'attitude_03_02', 'attitude_03_03', 'attitude_04_01', 'attitude_04_02', 'attitude_04_03', 'attitude_04_04', 'attitude_05_01', 'attitude_05_02', 'post_id']


class AbilityForm(forms.Form):
    email = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    department = forms.CharField(max_length=200)
    team = forms.CharField(max_length=200)
    level = forms.CharField(max_length=200)
    ability_01_01 = forms.CharField(max_length=200)
    ability_01_02 = forms.CharField(max_length=200)
    ability_02_01 = forms.CharField(max_length=200)
    ability_03_01 = forms.CharField(max_length=200)
    ability_03_02 = forms.CharField(max_length=200)
    ability_03_03 = forms.CharField(max_length=200)
    ability_04_01 = forms.CharField(max_length=200)
    ability_04_02 = forms.CharField(max_length=200)
    ability_05_01 = forms.CharField(max_length=200)
    ability_05_02 = forms.CharField(max_length=200)
    ability_06_01 = forms.CharField(max_length=200)
    ability_06_02 = forms.CharField(max_length=200)
    post_id = forms.CharField(max_length=200)

    class Meta:
        model = AbilityForm
        fields = ['id', 'email', 'name', 'department', 'team', 'level', 'ability_01_01', 'ability_01_02', 'ability_02_01', 'ability_03_01', 'ability_03_02', 'ability_03_03', 'ability_04_01', 'ability_04_02', 'ability_05_01', 'ability_05_02', 'ability_06_01', 'ability_06_02', 'post_id']


class AchievementForm(forms.Form):
    email = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    department = forms.CharField(max_length=200)
    team = forms.CharField(max_length=200)
    level = forms.CharField(max_length=200)
    achievement_01_01 = forms.CharField(max_length=200)
    achievement_02_01 = forms.CharField(max_length=200)
    post_id = forms.CharField(max_length=200)

    class Meta:
        model = AchievementForm
        fields = ['id', 'email', 'name', 'department', 'team', 'level', 'achievement_01_01', 'achievement_02_01', 'post_id']
        

class ScheduleForm(forms.Form):
    email = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    department = forms.CharField(max_length=200)
    team = forms.CharField(max_length=200)
    level = forms.CharField(max_length=200)
    schedule_01_01 = forms.CharField(max_length=200)
    schedule_02_01 = forms.CharField(max_length=200)
    schedule_03_01 = forms.CharField(max_length=200)
    schedule_04_01 = forms.CharField(max_length=200)
    schedule_04_02 = forms.CharField(max_length=200)
    post_id = forms.CharField(max_length=200)

    class Meta:
        model =  ScheduleForm
        fields = ['id', 'email', 'name', 'department', 'team', 'level', 'schedule_01_01', 'schedule_02_01', 'schedule_03_01', 'schedule_04_01', 'schedule_04_02', 'post_id']


class ReportForm(forms.Form):
    email = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    department = forms.CharField(max_length=200)
    team = forms.CharField(max_length=200)
    level = forms.CharField(max_length=200)
    report_01_01 = forms.CharField(max_length=200)
    report_01_02 = forms.CharField(max_length=200)
    report_02_01 = forms.CharField(max_length=200)
    report_02_02 = forms.CharField(max_length=200)
    report_03_01 = forms.CharField(max_length=200)
    report_03_02 = forms.CharField(max_length=200)
    report_04_01 = forms.CharField(max_length=200)
    report_04_02 = forms.CharField(max_length=200)
    report_05_01 = forms.CharField(max_length=200)
    report_05_02 = forms.CharField(max_length=200)
    report_06_01 = forms.CharField(max_length=200)
    report_06_02 = forms.CharField(max_length=200)
    report_07_01 = forms.CharField(max_length=200)
    report_07_02 = forms.CharField(max_length=200)
    post_id = forms.CharField(max_length=200)

    class Meta:
        model =  ReportForm
        fields = ['id', 'email', 'name', 'department', 'team', 'level', 'report_01_01', 'report_01_02', 'report_02_01', 'report_02_02', 'report_03_01', 'report_03_02', 'report_04_01', 'report_04_02', 'report_05_01', 'report_05_02', 'report_06_01', 'report_06_02', 'report_07_01', 'report_07_02', 'post_id']



class ReportETCForm(forms.Form):
    email = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    department = forms.CharField(max_length=200)
    team = forms.CharField(max_length=200)
    level = forms.CharField(max_length=200)
    report_etc_01_01 = forms.CharField(max_length=200)
    report_etc_02_01 = forms.CharField(max_length=200)
    report_etc_03_01 = forms.CharField(max_length=200)
    post_id = forms.CharField(max_length=200)

    class Meta:
        model =  ReportETCForm
        fields = ['id', 'email', 'name', 'department', 'team', 'level', 'report_etc_01_01', 'report_etc_02_01', 'report_etc_03_01', 'post_id']
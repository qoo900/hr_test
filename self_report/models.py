from django.db import models
from django.conf import settings
from django import forms
from django.db.models import fields 
from accounts.models import User


class AttitudeModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    attitude_01_01 = models.CharField(max_length=200)
    attitude_01_02 = models.CharField(max_length=200)
    attitude_02_01 = models.CharField(max_length=200)
    attitude_02_02 = models.CharField(max_length=200)
    attitude_02_03 = models.CharField(max_length=200)
    attitude_02_04 = models.CharField(max_length=200)
    attitude_03_01 = models.CharField(max_length=200)
    attitude_03_02 = models.CharField(max_length=200)
    attitude_03_03 = models.CharField(max_length=200)
    attitude_04_01 = models.CharField(max_length=200)
    attitude_04_02 = models.CharField(max_length=200)
    attitude_04_03 = models.CharField(max_length=200)
    attitude_04_04 = models.CharField(max_length=200)
    attitude_05_01 = models.CharField(max_length=200)
    attitude_05_02 = models.CharField(max_length=200)
    post_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="foreign_key")


class AttitudeForm(forms.ModelForm):
    class Meta:
        model = AttitudeModel
        fields = ['id', 'email', 'name', 'department', 'team', 'level', 'attitude_01_01', 'attitude_01_02', 'attitude_02_01', 'attitude_02_02', 'attitude_02_03', 'attitude_02_04', 'attitude_03_01', 'attitude_03_02', 'attitude_03_03', 'attitude_04_01', 'attitude_04_02', 'attitude_04_03', 'attitude_04_04', 'attitude_05_01', 'attitude_05_02', 'post_id']


class AbilityModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    ability_01_01 = models.CharField(max_length=200)
    ability_01_02 = models.CharField(max_length=200)
    ability_02_01 = models.CharField(max_length=200)
    ability_03_01 = models.CharField(max_length=200)
    ability_03_02 = models.CharField(max_length=200)
    ability_03_03 = models.CharField(max_length=200)
    ability_04_01 = models.CharField(max_length=200)
    ability_04_02 = models.CharField(max_length=200)
    ability_05_01 = models.CharField(max_length=200)
    ability_05_02 = models.CharField(max_length=200)
    ability_06_01 = models.CharField(max_length=200)
    ability_06_02 = models.CharField(max_length=200)
    post_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="foreign_key")


class AbilityForm(forms.ModelForm):
    class Meta:
        model = AbilityModel
        fields = ['id', 'email', 'name', 'department', 'team', 'level', 'ability_01_01', 'ability_01_02', 'ability_02_01', 'ability_03_01', 'ability_03_02', 'ability_03_03', 'ability_04_01', 'ability_04_02', 'ability_05_01', 'ability_05_02', 'ability_06_01', 'ability_06_02', 'post_id']


class AchievementModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    achievement_01_01 = models.CharField(max_length=200)
    achievement_02_01 = models.CharField(max_length=200)
    post_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="foreign_key")


class AchievementForm(forms.ModelForm):
    class Meta:
        model = AchievementModel
        fields = ['id', 'email', 'name', 'department', 'team', 'level', 'achievement_01_01', 'achievement_02_01', 'post_id']
        

class ScheduleModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    schedule_01_01 = models.CharField(max_length=200)
    schedule_02_01 = models.CharField(max_length=200)
    schedule_03_01 = models.CharField(max_length=200)
    schedule_04_01 = models.CharField(max_length=200)
    schedule_04_02 = models.CharField(null=True,max_length=200)
    post_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="foreign_key")


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = ScheduleModel
        fields = ['id', 'email', 'name', 'department', 'team', 'level', 'schedule_01_01', 'schedule_02_01', 'schedule_03_01', 'schedule_04_01', 'schedule_04_02', 'post_id']
        
class ReportModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    report_01_01 = models.CharField(max_length=200)
    report_01_02 = models.CharField(max_length=200)
    report_02_01 = models.CharField(max_length=200)
    report_02_02 = models.CharField(max_length=200)
    report_03_01 = models.CharField(max_length=200)
    report_03_02 = models.CharField(max_length=200)
    report_04_01 = models.CharField(null=True,max_length=200)
    report_04_02 = models.CharField(null=True,max_length=200)
    report_05_01 = models.CharField(null=True,max_length=200)
    report_05_02 = models.CharField(null=True,max_length=200)
    report_06_01 = models.CharField(null=True,max_length=200)
    report_06_02 = models.CharField(null=True,max_length=200)
    report_07_01 = models.CharField(null=True,max_length=200)
    report_07_02 = models.CharField(null=True,max_length=200)
    post_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="foreign_key")


class ReportForm(forms.ModelForm):
    class Meta:
        model = ReportModel
        fields = ['id', 'email', 'name', 'department', 'team', 'level', 'report_01_01', 'report_01_02', 'report_02_01', 'report_02_02', 'report_03_01', 'report_03_02', 'report_04_01', 'report_04_02', 'report_05_01', 'report_05_02', 'report_06_01', 'report_06_02', 'report_07_01', 'report_07_02', 'post_id']
        

class ReportETCModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    report_etc_01_01 = models.CharField(max_length=200)
    report_etc_02_01 = models.CharField(max_length=200)
    report_etc_03_01 = models.CharField(max_length=200)
    post_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="foreign_key")


class ReportETCForm(forms.ModelForm):
    class Meta:
        model = ReportETCModel
        fields = ['id', 'email', 'name', 'department', 'team', 'level', 'report_etc_01_01', 'report_etc_02_01', 'report_etc_03_01', 'post_id']
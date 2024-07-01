from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .models import AttitudeForm, AttitudeModel, AbilityForm, AbilityModel, AchievementForm, AchievementModel, ScheduleForm, ScheduleModel, ReportForm, ReportModel, ReportETCForm, ReportETCModel

# Create your views here.



#자기평가 메인
@login_required
def self_home (request):  
    user_list = User.objects.filter(email=f"{request.user.email}")
    i_name = []
    i_level = []
    i_email = []
    i_team = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
        i_team.append(iname.team)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    user_team = i_team[0]
    
    users_url=[]
    is_name = []
    is_level = []
    is_email = []
    is_team = []
    if user_level == "1":
        users_list = User.objects.all()
        for user_list in users_list:
            users_url.append(user_list.password)
        for isname in users_list:
            is_name.append(isname.name)
            is_level.append(isname.level)
            is_email.append(isname.email)
            is_team.append(isname.team)
        users_name = is_name
        users_level = is_level
        users_email = is_email
        users_team = is_team
    
    if user_level == "2":
        users_list = User.objects.filter(department=f"{request.user.department}")
        for user_list in users_list:
            users_url.append(user_list.password)
        for isname in users_list:
            is_name.append(isname.name)
            is_level.append(isname.level)
            is_email.append(isname.email)
            is_team.append(isname.team)
        users_name = is_name
        users_level = is_level
        users_email = is_email
        users_team = is_team
        

    if user_level == "3":
        users_list = User.objects.filter(team=f"{request.user.team}")
        for user_list in users_list:
            users_url.append(user_list.password)
        for isname in users_list:
            is_name.append(isname.name)
            is_level.append(isname.level)
            is_email.append(isname.email)
            is_team.append(isname.team)
        users_name = is_name
        users_level = is_level
        users_email = is_email
        users_team = is_team

    if user_level == "4":
        users_list = User.objects.filter(email=f"{request.user.email}")
        for user_list in users_list:
            users_url.append(user_list.password)
        for isname in users_list:
            is_name.append(isname.name)
            is_level.append(isname.level)
            is_email.append(isname.email)
            is_team.append(isname.team)
        users_name = is_name
        users_level = is_level
        users_email = is_email
        users_team = is_team

    #users_list = get_object_or_404(User)
    return render(request, 'self_home.html',
                  {'name':users_name,
                   'level':users_level,
                   'team':users_team,
                   'users_list':users_list, 
                   'users_url':users_url, 
                   'user_level':user_level,
                   'title':'2024년도 자기평가서 고과대상', 'pageview':'2024년도 자기평가서'})

#자기평가 상세
@login_required
def self_detail (request, pk):
    users_detail = User.objects.get(pk=pk)
    user_list = User.objects.filter(email=f"{users_detail.email}")
    i_name = []
    i_level = []
    i_email = []
    i_team = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
        i_team.append(iname.team)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    user_team = i_team[0]
    return render(request, 'self_detail.html', {'users_detail':users_detail, 'name':user_name, 'team':user_team, 'title':'2024년도 자기평가서 고과대상', 'pageview':'2024년도 자기평가서'})


#자기평가 태도 작성
@login_required
def self_post_attitude (request, pk):
    users_detail = User.objects.get(pk=pk)
    user_list = User.objects.filter(email=f"{users_detail.email}")
    i_name = []
    i_level = []
    i_email = []
    i_team = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
        i_team.append(iname.team)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    user_team = i_team[0]
    user_level_001 = str(int(user_level)-1)
    user_level_002 = str(int(user_level_001)-1)
    user_level_003 = str(int(user_level_002)-1)
    
    report_detail_001 = AttitudeModel.objects.filter(email=f"{users_detail.email}", level=f"{users_detail.level}")
    report_detail_002 = AttitudeModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_001}")
    report_detail_003 = AttitudeModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_002}")
    report_detail_004 = AttitudeModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_003}")

    
    return render(request, 'self_post_attitude.html', {'report_detail_001': report_detail_001, 'report_detail_002': report_detail_002, 'report_detail_003': report_detail_003, 'report_detail_004': report_detail_004, 'users_detail':users_detail, 'name':user_name, 'user_name':user_name, 'user_level' : user_level, 'user_email' : user_email, 'user_team':user_team, 'title':'2024년도 자기평가서 (태도)', 'pageview':'2024년도 자기평가서 작성'})


#자기평가 태도 평가제출
@login_required
def self_submit_attitude (request, pk):
    users_detail = User.objects.get(pk=pk)
    pk = str(users_detail.id)
    
    self_delete_attitude = AttitudeModel.objects.filter(email=f"{users_detail.email}").filter(name=f"{request.user.name}")
    self_delete_attitude.delete()
    
    user_list = User.objects.filter(email=f"{users_detail.email}")
    i_name = []
    i_level = []
    i_email = []
    i_team = []
    i_department = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
        i_department.append(iname.department)
        i_team.append(iname.team)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    user_team = i_team[0]
    user_department = i_department[0]
    
    email = user_email
    name = request.user.name
    department = user_department
    team = user_team
    level = request.user.level
    
    if request.method == "POST":
       
        attitude_01_01 = request.POST.get("attitude_01_01")
        attitude_01_02 = request.POST.get("attitude_01_02")
        
        attitude_02_01 = request.POST.get("attitude_02_01")
        attitude_02_02 = request.POST.get("attitude_02_02")
        attitude_02_03 = request.POST.get("attitude_02_03")
        attitude_02_04 = request.POST.get("attitude_02_04")
        
        attitude_03_01 = request.POST.get("attitude_03_01")
        attitude_03_02 = request.POST.get("attitude_03_02")
        attitude_03_03 = request.POST.get("attitude_03_03")
        
        attitude_04_01 = request.POST.get("attitude_04_01")
        attitude_04_02 = request.POST.get("attitude_04_02")
        attitude_04_03 = request.POST.get("attitude_04_03")
        attitude_04_04 = request.POST.get("attitude_04_04")
        
        attitude_05_01 = request.POST.get("attitude_05_01")
        attitude_05_02 = request.POST.get("attitude_05_02")

        ready_form = {'email' : email,
                      'name' : name,
                      'department' : department,
                      'team' : team,
                      'level' : level,
                      'attitude_01_01' : attitude_01_01,
                      'attitude_01_02' : attitude_01_02,
                      'attitude_02_01' : attitude_02_01,
                      'attitude_02_02' : attitude_02_02,
                      'attitude_02_03' : attitude_02_03,
                      'attitude_02_04' : attitude_02_04,
                      'attitude_03_01' : attitude_03_01,
                      'attitude_03_02' : attitude_03_02,
                      'attitude_03_03' : attitude_03_03,
                      'attitude_04_01' : attitude_04_01,
                      'attitude_04_02' : attitude_04_02, 
                      'attitude_04_03' : attitude_04_03,
                      'attitude_04_04' : attitude_04_04,
                      'attitude_05_01' : attitude_05_01,
                      'attitude_05_02' : attitude_05_02,
                      'post_id' : pk}
    
        filled_form = AttitudeForm(ready_form)
        if filled_form.is_valid():
            filled_form.save()
    return render(request, 'self_detail.html', {'users_detail':users_detail, 'name':user_name, 'user_name':user_name, 'user_level' : user_level, 'user_email' : user_email, 'user_team':user_team, 'title':'2024년도 자기평가서 (태도)', 'pageview':'2024년도 자기평가서 작성'})


#자기평가 능력 작성
@login_required
def self_post_ability (request, pk):
    users_detail = User.objects.get(pk=pk)
    user_list = User.objects.filter(email=f"{users_detail.email}")
    i_name = []
    i_level = []
    i_email = []
    i_team = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
        i_team.append(iname.team)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    user_team = i_team[0]
    
    user_level_001 = str(int(user_level)-1)
    user_level_002 = str(int(user_level_001)-1)
    user_level_003 = str(int(user_level_002)-1)
    
    report_detail_001 = AbilityModel.objects.filter(email=f"{users_detail.email}", level=f"{users_detail.level}")
    report_detail_002 = AbilityModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_001}")
    report_detail_003 = AbilityModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_002}")
    report_detail_004 = AbilityModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_003}")

    return render(request, 'self_post_ability.html', {'report_detail_001': report_detail_001, 'report_detail_002': report_detail_002, 'report_detail_003': report_detail_003, 'report_detail_004': report_detail_004, 'users_detail':users_detail, 'name':user_name, 'user_name':user_name, 'user_level' : user_level, 'user_email' : user_email, 'user_team':user_team, 'title':'2024년도 자기평가서 (능력)', 'pageview':'2024년도 자기평가서 작성'})


#자기평가 능력 평가제출
@login_required
def self_submit_ability (request, pk):
    users_detail = User.objects.get(pk=pk)
    pk = str(users_detail.id)
    
    self_delete_ability = AbilityModel.objects.filter(email=f"{users_detail.email}").filter(name=f"{request.user.name}")
    self_delete_ability.delete()
    
    user_list = User.objects.filter(email=f"{users_detail.email}")
    i_name = []
    i_level = []
    i_email = []
    i_team = []
    i_department = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
        i_department.append(iname.department)
        i_team.append(iname.team)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    user_team = i_team[0]
    user_department = i_department[0]
    
    email = user_email
    name = request.user.name
    department = user_department
    team = user_team
    level = request.user.level
    
    if request.method == "POST":
       
        ability_01_01 = request.POST.get("ability_01_01")
        ability_01_02 = request.POST.get("ability_01_02")
        
        ability_02_01 = request.POST.get("ability_02_01")
        
        ability_03_01 = request.POST.get("ability_03_01")
        ability_03_02 = request.POST.get("ability_03_02")
        ability_03_03 = request.POST.get("ability_03_03")
        
        ability_04_01 = request.POST.get("ability_04_01")
        ability_04_02 = request.POST.get("ability_04_02")
                                         
        ability_05_01 = request.POST.get("ability_05_01")
        ability_05_02 = request.POST.get("ability_05_02")
        
        ability_06_01 = request.POST.get("ability_06_01")
        ability_06_02 = request.POST.get("ability_06_02")

        ready_form = {'email' : email,
                      'name' : name,
                      'department' : department,
                      'team' : team,
                      'level' : level,
                      'ability_01_01' : ability_01_01,
                      'ability_01_02' : ability_01_02,
                      'ability_02_01' : ability_02_01,
                      'ability_03_01' : ability_03_01,
                      'ability_03_02' : ability_03_02,
                      'ability_03_03' : ability_03_03,
                      'ability_04_01' : ability_04_01,
                      'ability_04_02' : ability_04_02,
                      'ability_05_01' : ability_05_01,
                      'ability_05_02' : ability_05_02,
                      'ability_06_01' : ability_06_01,
                      'ability_06_02' : ability_06_02,
                      'post_id' : pk}
    
        filled_form = AbilityForm(ready_form)
        if filled_form.is_valid():
            filled_form.save()
    return render(request, 'self_detail.html', {'users_detail':users_detail, 'name':user_name, 'user_name':user_name, 'user_level' : user_level, 'user_email' : user_email, 'user_team':user_team, 'title':'2024년도 자기평가서 (능력)', 'pageview':'2024년도 자기평가서 작성'})


#자기평가 업적 작성
@login_required
def self_post_achievement (request, pk):
    users_detail = User.objects.get(pk=pk)
    user_list = User.objects.filter(email=f"{users_detail.email}")
    i_name = []
    i_level = []
    i_email = []
    i_team = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
        i_team.append(iname.team)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    user_team = i_team[0]
    
    user_level_001 = str(int(user_level)-1)
    user_level_002 = str(int(user_level_001)-1)
    user_level_003 = str(int(user_level_002)-1)
    
    report_detail_001 = AchievementModel.objects.filter(email=f"{users_detail.email}", level=f"{users_detail.level}")
    report_detail_002 = AchievementModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_001}")
    report_detail_003 = AchievementModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_002}")
    report_detail_004 = AchievementModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_003}")
    
    report_detail_report_001 = ReportModel.objects.filter(email=f"{users_detail.email}", level=f"{users_detail.level}")

    
    return render(request, 'self_post_achievement.html', {'report_detail_report_001':report_detail_report_001, 'report_detail_001': report_detail_001, 'report_detail_002': report_detail_002, 'report_detail_003': report_detail_003, 'report_detail_004': report_detail_004, 'users_detail':users_detail, 'name':user_name, 'user_name':user_name, 'user_level' : user_level, 'user_email' : user_email, 'user_team':user_team, 'title':'2024년도 자기평가서 (업적)', 'pageview':'2024년도 자기평가서 작성'})


#자기평가 업적 평가제출
@login_required
def self_submit_achievement (request, pk):
    users_detail = User.objects.get(pk=pk)
    pk = str(users_detail.id)
    
    self_delete_achievement = AchievementModel.objects.filter(email=f"{users_detail.email}").filter(name=f"{request.user.name}")
    self_delete_achievement.delete()
    
    user_list = User.objects.filter(email=f"{users_detail.email}")
    i_name = []
    i_level = []
    i_email = []
    i_team = []
    i_department = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
        i_department.append(iname.department)
        i_team.append(iname.team)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    user_team = i_team[0]
    user_department = i_department[0]
    
    email = user_email
    name = request.user.name
    department = user_department
    team = user_team
    level = request.user.level
    
    if request.method == "POST":
       
        achievement_01_01 = request.POST.get("achievement_01_01")
        achievement_02_01 = request.POST.get("achievement_02_01")

        ready_form = {'email' : email,
                      'name' : name,
                      'department' : department,
                      'team' : team,
                      'level' : level,
                      
                      'achievement_01_01' : achievement_01_01,
                      'achievement_02_01' : achievement_02_01,
                      
                      'post_id' : pk}
    
        filled_form = AchievementForm(ready_form)
        if filled_form.is_valid():
            filled_form.save()
    return render(request, 'self_detail.html', {'users_detail':users_detail, 'name':user_name, 'user_name':user_name, 'user_level' : user_level, 'user_email' : user_email, 'user_team':user_team, 'title':'2024년도 자기평가서 (업적)', 'pageview':'2024년도 자기평가서 작성'})



#자기평가 직무상황 작성
@login_required
def self_post_schedule (request, pk):
    users_detail = User.objects.get(pk=pk)
    user_list = User.objects.filter(email=f"{users_detail.email}")
    i_name = []
    i_level = []
    i_email = []
    i_team = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
        i_team.append(iname.team)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    user_team = i_team[0]
    
    user_level_001 = str(int(user_level)-1)
    user_level_002 = str(int(user_level_001)-1)
    user_level_003 = str(int(user_level_002)-1)
    
    report_detail_001 = ScheduleModel.objects.filter(email=f"{users_detail.email}", level=f"{users_detail.level}")
    report_detail_002 = ScheduleModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_001}")
    report_detail_003 = ScheduleModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_002}")
    report_detail_004 = ScheduleModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_003}")
    
    return render(request, 'self_post_schedule.html', {'report_detail_001': report_detail_001, 'report_detail_002': report_detail_002, 'report_detail_003': report_detail_003, 'report_detail_004': report_detail_004, 'users_detail':users_detail, 'name':user_name, 'user_name':user_name, 'user_level' : user_level, 'user_email' : user_email, 'user_team':user_team, 'title':'2024년도 자기평가서 (직무상황)', 'pageview':'2024년도 자기평가서 작성'})


#자기평가 직무상황 평가제출
@login_required
def self_submit_schedule (request, pk):
    users_detail = User.objects.get(pk=pk)
    pk = str(users_detail.id)
    
    self_delete_schedule = ScheduleModel.objects.filter(email=f"{users_detail.email}").filter(name=f"{request.user.name}")
    self_delete_schedule.delete()
    
    user_list = User.objects.filter(email=f"{users_detail.email}")
    i_name = []
    i_level = []
    i_email = []
    i_team = []
    i_department = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
        i_department.append(iname.department)
        i_team.append(iname.team)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    user_team = i_team[0]
    user_department = i_department[0]
    
    email = user_email
    name = request.user.name
    department = user_department
    team = user_team
    level = request.user.level
    
    if request.method == "POST":
       
        schedule_01_01 = request.POST.get("schedule_01_01")
        schedule_02_01 = request.POST.get("schedule_02_01")
        schedule_03_01 = request.POST.get("schedule_03_01")
        schedule_04_01 = request.POST.get("schedule_04_01")
        schedule_04_02 = request.POST.get("schedule_04_02")

        ready_form = {'email' : email,
                      'name' : name,
                      'department' : department,
                      'team' : team,
                      'level' : level,
                      
                      'schedule_01_01' : schedule_01_01,
                      'schedule_02_01' : schedule_02_01,
                      'schedule_03_01' : schedule_03_01,
                      'schedule_04_01' : schedule_04_01,
                      'schedule_04_02' : schedule_04_02,
                      
                      'post_id' : pk}
    
        filled_form = ScheduleForm(ready_form)
        if filled_form.is_valid():
            filled_form.save()
    return render(request, 'self_detail.html', {'users_detail':users_detail, 'name':user_name, 'user_name':user_name, 'user_level' : user_level, 'user_email' : user_email, 'user_team':user_team, 'title':'2024년도 자기평가서 (직무상황)', 'pageview':'2024년도 자기평가서 작성'})



#자기신고서 작성
@login_required
def self_post_report (request, pk):
    users_detail = User.objects.get(pk=pk)
    user_list = User.objects.filter(email=f"{users_detail.email}")
    i_name = []
    i_level = []
    i_email = []
    i_team = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
        i_team.append(iname.team)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    user_team = i_team[0]
    
    user_level_001 = str(int(user_level)-1)
    user_level_002 = str(int(user_level_001)-1)
    user_level_003 = str(int(user_level_002)-1)
    
    report_detail_001 = ReportModel.objects.filter(email=f"{users_detail.email}", level=f"{users_detail.level}")
    report_detail_002 = ReportModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_001}")
    report_detail_003 = ReportModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_002}")
    report_detail_004 = ReportModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_003}")
    
    return render(request, 'self_post_report.html', {'report_detail_001': report_detail_001, 'report_detail_002': report_detail_002, 'report_detail_003': report_detail_003, 'report_detail_004': report_detail_004, 'users_detail':users_detail, 'name':user_name, 'user_name':user_name, 'user_level' : user_level, 'user_email' : user_email, 'user_team':user_team, 'title':'2024년도 자기신고서 작성', 'pageview':'2024년도 자기평가서 고과대상'})


#자기신고서 평가제출
@login_required
def self_submit_report (request, pk):
    users_detail = User.objects.get(pk=pk)
    pk = str(users_detail.id)
    
    self_delete_report = ReportModel.objects.filter(email=f"{users_detail.email}").filter(name=f"{request.user.name}")
    self_delete_report.delete()
    
    user_list = User.objects.filter(email=f"{users_detail.email}")
    i_name = []
    i_level = []
    i_email = []
    i_team = []
    i_department = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
        i_department.append(iname.department)
        i_team.append(iname.team)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    user_team = i_team[0]
    user_department = i_department[0]
    
    email = user_email
    name = request.user.name
    department = user_department
    team = user_team
    level = request.user.level
    
    if request.method == "POST":
       
        report_01_01 = request.POST.get("report_01_01")
        report_01_02 = request.POST.get("report_01_02")
        
        report_02_01 = request.POST.get("report_02_01")
        report_02_02 = request.POST.get("report_02_02")
        
        report_03_01 = request.POST.get("report_03_01")
        report_03_02 = request.POST.get("report_03_02")
        
        report_04_01 = request.POST.get("report_04_01")
        report_04_02 = request.POST.get("report_04_02")
        
        report_05_01 = request.POST.get("report_05_01")
        report_05_02 = request.POST.get("report_05_02")
        
        report_06_01 = request.POST.get("report_06_01")
        report_06_02 = request.POST.get("report_06_02")
        
        report_07_01 = request.POST.get("report_07_01")
        report_07_02 = request.POST.get("report_07_02")

        ready_form = {'email' : email,
                      'name' : name,
                      'department' : department,
                      'team' : team,
                      'level' : level,
                      'report_01_01' : report_01_01,
                      'report_01_02' : report_01_02,
                      'report_02_01' : report_02_01,
                      'report_02_02' : report_02_02,
                      'report_03_01' : report_03_01,
                      'report_03_02' : report_03_02,
                      'report_04_01' : report_04_01,
                      'report_04_02' : report_04_02,
                      'report_05_01' : report_05_01,
                      'report_05_02' : report_05_02,
                      'report_06_01' : report_06_01,
                      'report_06_02' : report_06_02,
                      'report_07_01' : report_07_01,
                      'report_07_02' : report_07_02,
                      'post_id' : pk}
    
        filled_form = ReportForm(ready_form)
        if filled_form.is_valid():
            filled_form.save()
    return render(request, 'self_detail.html', {'users_detail':users_detail, 'name':user_name, 'user_name':user_name, 'user_level' : user_level, 'user_email' : user_email, 'user_team':user_team, 'title':'2024년도 자기신고서', 'pageview':'2024년도 자기평가서 작성'})



#자기신고서 (기타사항) 작성
@login_required
def self_post_report_etc (request, pk):
    users_detail = User.objects.get(pk=pk)
    user_list = User.objects.filter(email=f"{users_detail.email}")
    i_name = []
    i_level = []
    i_email = []
    i_team = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
        i_team.append(iname.team)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    user_team = i_team[0]
    
    user_level_001 = str(int(user_level)-1)
    user_level_002 = str(int(user_level_001)-1)
    user_level_003 = str(int(user_level_002)-1)
    
    report_detail_001 = ReportETCModel.objects.filter(email=f"{users_detail.email}", level=f"{users_detail.level}")
    report_detail_002 = ReportETCModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_001}")
    report_detail_003 = ReportETCModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_002}")
    report_detail_004 = ReportETCModel.objects.filter(email=f"{users_detail.email}", level=f"{user_level_003}")
    
    return render(request, 'self_post_report_etc.html', {'report_detail_001': report_detail_001, 'report_detail_002': report_detail_002, 'report_detail_003': report_detail_003, 'report_detail_004': report_detail_004, 'users_detail':users_detail, 'name':user_name, 'user_name':user_name, 'user_level' : user_level, 'user_email' : user_email, 'user_team':user_team, 'title':'2024년도 자기신고서 작성', 'pageview':'2024년도 자기평가서 고과대상'})



#자기신고서 평가제출
@login_required
def self_submit_report_etc (request, pk):
    users_detail = User.objects.get(pk=pk)
    pk = str(users_detail.id)
    
    self_delete_report = ReportETCModel.objects.filter(email=f"{users_detail.email}").filter(name=f"{request.user.name}")
    self_delete_report.delete()
    
    user_list = User.objects.filter(email=f"{users_detail.email}")
    i_name = []
    i_level = []
    i_email = []
    i_team = []
    i_department = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
        i_department.append(iname.department)
        i_team.append(iname.team)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    user_team = i_team[0]
    user_department = i_department[0]
    
    email = user_email
    name = request.user.name
    department = user_department
    team = user_team
    level = request.user.level
    
    if request.method == "POST":
       
        report_etc_01_01 = request.POST.get("report_etc_01_01")    
        report_etc_02_01 = request.POST.get("report_etc_02_01") 
        report_etc_03_01 = request.POST.get("report_etc_03_01")

        ready_form = {'email' : email,
                      'name' : name,
                      'department' : department,
                      'team' : team,
                      'level' : level,
                      'report_etc_01_01' : report_etc_01_01,
                      'report_etc_02_01' : report_etc_02_01,
                      'report_etc_03_01' : report_etc_03_01,
                      'post_id' : pk}
    
        filled_form = ReportETCForm(ready_form)
        if filled_form.is_valid():
            filled_form.save()
    return render(request, 'self_detail.html', {'users_detail':users_detail, 'name':user_name, 'user_name':user_name, 'user_level' : user_level, 'user_email' : user_email, 'user_team':user_team, 'title':'2024년도 자기신고서', 'pageview':'2024년도 자기평가서 작성'})


from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.views.decorators.http import require_http_methods
from django.contrib import messages


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('self_home')
        else: 
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')


def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            if new_user is not None:
                # 로그인
                auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
                # 홈 리다이렉션
                return redirect('home')
        else: 
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')


@login_required
@require_http_methods(["GET", "POST"])
def reset_password(request):
    context= {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password,user.password):
            new_password = request.POST.get("reset_password")
            password_confirm = request.POST.get("reset_repeat")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                auth.logout(request)
                return redirect("login")
            else:
                messages.warning(request, "신규 비밀번호를 다시 확인해주세요.")
                return redirect("reset_password")
        else:
            messages.warning(request, "기존 비밀번호가 일치하지 않습니다.")
            return redirect("reset_password")
    else:
        return render(request, 'reset_password.html', {'context':context})
    pass
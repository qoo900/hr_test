from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, FreeCommentForm, FreePostForm
from .models import Post, FreePost
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from accounts.models import User



def home(request):
    user_list = User.objects.filter(email=f"{request.user.email}")
    i_name = []
    i_level = []
    i_email = []
    for iname in user_list:
        i_name.append(iname.name)
        i_level.append(iname.level)
        i_email.append(iname.email)
    user_name = i_name[0]
    user_level = i_level[0]
    user_email = i_email[0]
    
    users_url=[]
    if user_level == "1":
        users_list = User.objects.all()
        for user_list in users_list:
            users_url.append(user_list.password)
    
    if user_level == "2":
        users_list = User.objects.filter(department=f"{request.user.department}")
        for user_list in users_list:
            users_url.append(user_list.password)
        

    if user_level == "3":
        users_list = User.objects.filter(team=f"{request.user.team}")
        for user_list in users_list:
            users_url.append(user_list.password)

    if user_level == "4":
        users_list = User.objects.filter(email=f"{request.user.email}")
        for user_list in users_list:
            users_url.append(user_list.password)

    #users_list = get_object_or_404(User)
    return render(request, 'index.html', 
                  {'name':user_name,
                    'users_list':users_list, 
                   'users_url':users_url, 
                   'title':'대시보드', 
                   'pageview':'Trendmecca-HR'})


#근태관리 확인용(TEST)
def attendance(request):
    # posts = Post.objects.all()
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'attendance_index.html', {'freeposts': freeposts, 'title':'문의게시판', 'pageview':'Trendmecca-HR'})



@login_required
def postcreate(request):
    # request method가 POST일 경우  
    # 입력값 저장
    # request method가 GET인 경우
    # form 입력 html 띄우기
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})


def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form': comment_form})


# 댓글 저장
def new_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect('detail', post_id)

#게시판
def freehome(request):
    # posts = Post.objects.all()
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'free_index.html', {'freeposts': freeposts, 'title':'문의게시판', 'pageview':'Trendmecca-HR'})

#게시판 글쓰기
@login_required
def freepostcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user            # user 추가!
            unfinished.save()
            return redirect('freehome')
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form':form, 'title':'글쓰기', 'pageview':'문의게시판'})

#게시판 상세페이지
def freedetail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form': comment_form, 'title':'상세페이지', 'pageview':'문의게시판'})

#게시판 댓글추가
def new_freecomment(request, post_id):
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.save()
    return redirect('freedetail', post_id)


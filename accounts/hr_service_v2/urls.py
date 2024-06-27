"""hr_service_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from snsapp import views as snsapp_views
from accounts import views as accounts_views
from self_report import views as self_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('index', snsapp_views.home, name='home'),
    path('postcreate', snsapp_views.postcreate, name='postcreate'),
    
    path('detail/<int:post_id>', snsapp_views.detail, name='detail'),
    path('new_comment/<int:post_id>', snsapp_views.new_comment, name='new_comment'),
    
    path('freehome/', snsapp_views.freehome, name='freehome'),
    path('freepostcreate', snsapp_views.freepostcreate, name='freepostcreate'),
    path('freedetail/<int:post_id>', snsapp_views.freedetail, name='freedetail'),
    path('new_freecomment/<int:post_id>', snsapp_views.new_freecomment, name='new_freecomment'),
    
    path('', accounts_views.login, name='login'),
    path('reset_password/', accounts_views.reset_password, name='reset_password'), 
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),

    path('accounts/', include('allauth.urls')),

    path('self_home', self_views.self_home, name='self_home'),
    
    path('self_detail/<int:pk>', self_views.self_detail, name='self_detail'),
    
    path('self_post_attitude/<int:pk>', self_views.self_post_attitude, name='self_post_attitude'),
    path('self_submit_attitude/<int:pk>', self_views.self_submit_attitude, name='self_submit_attitude'),

    path('self_post_ability/<int:pk>', self_views.self_post_ability, name='self_post_ability'),
    path('self_submit_ability/<int:pk>', self_views.self_submit_ability, name='self_submit_ability'),

    path('self_post_achievement/<int:pk>', self_views.self_post_achievement, name='self_post_achievement'),   
    path('self_submit_achievement/<int:pk>', self_views.self_submit_achievement, name='self_submit_achievement'),   

    path('self_post_schedule/<int:pk>', self_views.self_post_schedule, name='self_post_schedule'),
    path('self_submit_schedule/<int:pk>', self_views.self_submit_schedule, name='self_submit_schedule'),
    
    path('self_post_report/<int:pk>', self_views.self_post_report, name='self_post_report'),
    path('self_submit_report/<int:pk>', self_views.self_submit_report, name='self_submit_report'),
    
    path('self_post_report_etc/<int:pk>', self_views.self_post_report_etc, name='self_post_report_etc'),
    path('self_submit_report_etc/<int:pk>', self_views.self_submit_report_etc, name='self_submit_report_etc'),    
    
    #path('self_delete_attitude/<int:pk>', self_views.self_delete_attitude, name='self_delete_attitude'),
    
]

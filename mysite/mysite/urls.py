"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url
from hrm.api import UserList, UserDetail, UserAuthentication
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('weather/', include('weather.urls')),
    path('budget/', include('budget.urls')),
    url(r'^api/users_list/$', UserList.as_view(), name='user_list'),
    url(r'^api/users_list/(?P<job_seeker_id>\d+)/$', UserDetail.as_view(), name='user_list'),
    url(r'^api/auth/$', UserAuthentication.as_view(), name='User Authentication API'),
    path('employee/', include('employee.urls')),    
]

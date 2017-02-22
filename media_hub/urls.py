"""media_hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from login_system.views import UserFormView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^reg/$', UserFormView.as_view(), name='reg'),
    url(r'^home/', include('website.urls')),
    url(r'^$', views.login,  {'template_name': 'login_system/login.html'}, name='login'),
    url(r'^logout/$', views.logout, {'template_name': 'login_system/logout.html'}, name='logout'),
    url(r'^job/', include('submit.urls')),
    url(r'^repo/', include('asset_db.urls')),
]
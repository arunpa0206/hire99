"""hire99 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from sourcingapp.forms import LoginForm
from sourcingapp import views as sourcingapp_views
from searchapp import views as searchapp_views
from dashing.utils import router

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('sourcingapp.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
    url(r'^signup/$', sourcingapp_views.signup, name='signup'),

    # Forgot Password URLs
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    # Signup Confirmation email
    url(r'^account_activation_sent/$', sourcingapp_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            sourcingapp_views.activate, name='activate'),

    # Job search page
    url(r'^jobsearch/$', searchapp_views.jobsearch, name='jobsearch'),
    #url(r'^jobsearch/$', searchapp_views.JobSearchView.as_view(), name='jobsearch'),

    # Detail page
    url(r'^jobdetail/$', searchapp_views.jobdetail, name='jobdetail'),

    # Candidate search page
    url(r'^candidatesearch/$', searchapp_views.candidatesearch, name='candidatesearch'),

    # Candidate forms
    url(r'^candidateform/$', searchapp_views.CandidateCreate.as_view()),

     url(r'^base/$', sourcingapp_views.base, name='base'),
]

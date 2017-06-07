# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import home, login, Dashboard

urlpatterns = [
  url(r'^$', home, name='home'),
  url(r'^login/$', login, name='login'),
  url(r'dashboard/$', Dashboard.as_view(), name='dashboard'),

  #url(r'login/$', LoginView.as_view(), name='login'),
]
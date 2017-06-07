# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.

def home(request):
  if request.user.is_authenticated():
    return HttpResponseRedirect(reverse('dashboard'))
  return render(request, 'login.html')


class Dashboard(TemplateView):
  template_name = 'dashboard.html'


def login(request):
  if request.POST:
    from pdb import set_trace
    set_trace()
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
      if user.is_active:
        auth_login(request, user)
        return HttpResponseRedirect(reverse('dashboard'))
  return render(request, 'login.html')



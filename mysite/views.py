#-*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from allauth.account.decorators import verified_email_required
from mysite import models

# Create your views here.

def index(request):
    return render(request, 'index.html', locals())




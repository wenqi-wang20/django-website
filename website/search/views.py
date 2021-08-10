import time
import pymysql
from django.shortcuts import render, redirect, reverse
from . import forms,models
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

def conn_sql():
    HOST = '121.4.27.125'
    USERNAME = 'root'
    DBNAME = 'webdata'
    PASSWORD = 'wwq2002620'
    db = pymysql.connect(user=USERNAME,password=PASSWORD,host=HOST,database=DBNAME,port=3306,charset='utf8mb4')
    return db


def home(request):
    title = "Search"
    content = "Your left brain has nothing right and your right brain has nothing left."
    return render(request, 'search/index.html', locals())

def search_list(request):
    start_time = time.time()
    searched = True
    keywords = request.GET.get('q')
    message = ''
    if not keywords:
        return redirect('/')
    words = keywords.split(' ')
####################

def login(request):
    if reverse('login'):
        if request.session.get('is_login', None):
            return redirect('/')
        if request.method == "POST":
            login_form = forms.UserForm(request.POST)
            message = "请检查填写的内容！"
            if login_form.is_valid():
                email = request.POST.get("email")
                password = request.POST.get("password")
                try:







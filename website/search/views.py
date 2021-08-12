import time
import pymysql
from django.shortcuts import render, redirect, reverse, HttpResponse
from . import forms,models
from .models import Poem,SearchUser,SearchHotspot
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

def conn_sql():
    HOST = '121.4.27.175'
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
    #return render(request, '/', locals())

    start_time = time.time()
    searched = True
    keywords = request.GET.get('q')
    print(keywords)
    message = ''
    if not keywords:
        return redirect('/')
    post_list = Poem.objects.order_by('id')
    post_list = post_list.filter(Q(author_name__contains=keywords) | Q(model_name__contains=keywords) | Q(poem_name__contains=keywords) | Q(dynasty__contains=keywords) | Q(content__contains=keywords))
    # try:
    #     old_word = SearchHotspot.object.get(word=keywords)
    # except:
    #     new_word = SearchHotspot()
    #     new_word.word = keywords
    #     new_word.count += 1
    #     new_word.save()
    # else:
    #     old_word.count += 1
    #     old_word.save()
    limit = 10
    paginator = Paginator(post_list, limit)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    end_time = time.time()
    load_time = end_time - start_time

    title = keywords + "- 众里寻他千百度"
    content = "蓦然回首，那人却在灯火阑珊处。"

    return render(request, 'search/result.html', locals())



def show_detail(request, post_id):
    try:
        post = Poem.objects.get(id=post_id)
    except:
        return redirect('/')
    ignore_list = ['id', 'title', 'body', 'url']
    params = [[f.verbose_name, post.__dict__[f.name]]
              for f in post._meta.fields if f.name not in ignore_list and post.__dict__[f.name]]

    title = post.poem_name
    content = post.content

    return render(request, 'search/detail.html', locals())



def login(request):
    print('before')
    if reverse('login'):
        print('after')
        if request.session.get('is_login', None):
            return redirect('/')
        if request.method == "POST":
            login_form = forms.UserForm(request.POST)
            message = "请检查填写的内容！"
            if login_form.is_valid():
                email = request.POST.get("email")
                password = request.POST.get("password")
                try:
                    user = models.SearchUser.objects.get(email=email)
                except:
                    message = "用户不存在！"
                    return render(request, "search/login.html", locals())
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_email'] = user.email
                    return redirect('/')
                else:
                    message = "密码不正确！"
                    return render(request, "search/login.html", locals())
            else:
                return render(request, "search/login.html", locals())
        login_form = forms.UserForm()

        title = "登入"
        content = "人生若只如初见，何事秋风悲画扇。"

        return render(request, "search/login.html", locals())


def signup(request):
    if reverse('signup'):
        if request.session.get("is_login", None):
            return redirect('/')
        if request.method == "POST":
            register_form = forms.RegisterForm(request.POST)
            message = "请检查填写的内容！"
            if register_form.is_valid():
                email = register_form.cleaned_data.get('email')
                password = register_form.cleaned_data.get('password')
                password_repeat = register_form.cleaned_data.get('password_repeat')
                if len(password) > 128:
                    message = "输入的密码过长！"
                    return render(request, 'search/signup.html', locals())
                elif password != password_repeat:
                   return render(request, 'search/signup.html', locals())
                else:
                    message = "两次输入的密码不一样！"
                    same_email_user = models.SearchUser.objects.filter(email=email)
                    if same_email_user:
                        message = '该邮箱已经被注册了！'
                        return render(request, 'search/signup.html', locals())
                    new_user = models.User()
                    new_user.email = email
                    new_user.password = password
                    if 'HTTP_X_FORWARDED_FOR' in request.META:
                        new_user.ip = request.META['HTTP_X_FORWARDED_FOR']
                    else:
                        new_user.ip = request.META['REMOTE_ADDR']
                    new_user.save()
                    request.session['is_login'] = True
                    request.session['user_email'] = email
                    return redirect('/')
            else:
                return render(request, 'search/signup.html', locals())
        register_form = forms.RegisterForm()

        title = "加入我们"
        content = "人生若只如初见，何事秋风悲画扇。"

        return render(request, 'search/signup.html', locals())

def logout(request):
    if reverse('logout') and request.session.get('is_login', None):
        request.session.flush()
    return redirect('/login/')



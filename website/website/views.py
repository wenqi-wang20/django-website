import time
from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

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
        return redirect('home/')
    words = keywords.split(' ')


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


from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('search/', views.search_list, name="search"),
    path('detail/<int:post_id>', views.show_detail),
]
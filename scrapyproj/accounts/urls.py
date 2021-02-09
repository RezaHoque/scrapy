from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout,name='logout'),
    path('users',views.users,name='users'),
#path('list',views.list,name='list')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scrap',views.scrap, name='scrap')
   # path('add',views.add,name='add'),
#path('list',views.list,name='list')
]
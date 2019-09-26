from django.urls import path
from . import views


urlpatterns =[
        path('',views.index, name='index'),
        path('gogetthegood/',views.gogetthegood, name='gettingthegood'),
        path('happyhappyjoyjoy/', views.happy, name ='happy'),
    path('new/<string>/', views.new,name='new'),
    ]
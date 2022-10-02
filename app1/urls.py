from django.urls import path
#now import the views.py file into this code
from django.urls import include, re_path
from app1 import views
urlpatterns=[
  path('',views.index)
]
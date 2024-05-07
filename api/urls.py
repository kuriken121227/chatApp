from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path(r'regist_user', views.regist_user, name='regist_user')
]
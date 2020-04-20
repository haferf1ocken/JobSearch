from django.conf.urls import url
from app import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url('user', views.getinfoUser),
    url('employer', views.getinfoEmployer),
    url('interships', views.getinfoIntership),
    url('login', views.login, name='login'),
    url('logout', views.logout, name='logout'),
]

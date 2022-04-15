
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include

from . import search, views, testDB, search_post, login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', login.login),
    url(r'^accounts/logout/$', login.logout),
    url(r'index/', views.hello),
    url(r'runoob/', views.runoob),
    url(r'testDB/', testDB.testDB),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search_post/$', search_post.search_post),
    path("emp/", include("TestForm.urls"))
]

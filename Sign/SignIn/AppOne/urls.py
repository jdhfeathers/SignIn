from django.contrib import admin
from django.urls import path, re_path
from AppOne import views
from django.conf.urls import include

from django.conf import settings
from django.conf.urls.static import static

app_name='AppOne'

urlpatterns=[
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^user_login/$',views.user_login, name='user_login'),
    re_path(r'^special/$',views.special, name='special'),

]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
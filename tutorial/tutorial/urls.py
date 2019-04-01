
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from community import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^write/', views.write, name='write'),
    url(r'^list/', views.list, name='list'),
]
 
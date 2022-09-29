from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views
import securite
from django.conf import settings
from django.conf.urls.static import static


app_name='securite'
urlpatterns = [
    path('', views.index, name = 'index'),
    url(r'^employees/create/$', views.employee_create, name ='employee_create'),
    url(r'^employees/(?P<pk>\d+)/update/$', views.employee_update, name ='employee_update'),
    url(r'^employees/(?P<pk>\d+)/delete/$', views.employee_delete, name ='employee_delete'),
    url(r'^employeeface/(?P<pk>\d+)/create/$', views.employeeface_create, name ='employeeface_create'),
    url(r'^notifications/(?P<pk>\d+)/$', views.notification_delete, name ='notification_delete'),
    url(r'^memberdetail/(?P<pk>\d+)/$', views.member_detail, name ='member_detail'),
    url('members/', views.members, name = 'members'),
    url('report/', views.report, name = 'report'),
    url('notifications/', views.notifications, name = 'notifications'),
    url('camera/', views.camera, name = 'camera'),
    url('intrusions/', views.intrusions, name = 'intrusions'),
    url('network/', views.network, name = 'network'),
    url('calendar/', views.calendar, name = 'calendar'),
    url(r'login/',views.login_user, name='login'),
    url(r'subscriber/',views.subscriber,name='subscriber'),
    url(r'^subscriberdetete/(?P<pk>\d+)/$', views.subscriber_delete, name ='subscriber_delete'),
    url(r'profile/',views.profile,name='profile'),
    url(r'door/',views.door,name='door'),

]
if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

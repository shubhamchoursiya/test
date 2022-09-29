from django.urls import path
from django.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from securite.views import FaceAPI,IpAPI,SubscriberAPI,NotificationAPI,EmployeeAPI,ProfileAPI,CustomAuthToken,CameraAPI
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
# app_name = 'Index'


urlpatterns = [
    url('userapi/',FaceAPI.as_view()),
#     url('proccesimage/',ProccesImage.as_view()),
    url('ipapi/',IpAPI.as_view()),
    url('subscriberapi/',SubscriberAPI),
    url('notificationapi/',NotificationAPI),
    url('employeeapi/',EmployeeAPI),
    url('profileapi/',ProfileAPI),
    url('cameraapi/',CameraAPI),
    url('api-token-auth/',CustomAuthToken.as_view()),
#     #url('userapi/',FaceAPI),
]

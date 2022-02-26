from django.contrib import admin
from django.urls import path
from doctorApp import views
admin.site.site_header = "Appointment Admin"
admin.site.index_title = "Welcome to AASTHA CLINIC"
admin.site.site_title = "Clinic Appointment "


urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginInd',views.loginInd),
    path('',views.loginIN),
    path('loginIN',views.loginIN),
    path('logOut',views.logOut), 
    path('regist',views.regist),
    path('newUser',views.newUser),
    path('index',views.index),
    path('about',views.about),
    path('about/',views.about),
    path('contact',views.contact),
    path('contact/',views.contact),
    path('booking',views.Appointment),
    path('cs_booking',views.csAppointment),
    path('fd_avl',views.fd_avl),
    path('fd_get',views.fd_get),
    path('pd_avl',views.pd_avl),
    path('pd_get',views.pd_get),
    path('dignos',views.dignos),
    path('counsult',views.counsult),
    path('admit',views.admit),
    path('nicu',views.nicu),
    
    
]

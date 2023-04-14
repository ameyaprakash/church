
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
   path('login/',views.login,name="login"),
    path('login_post/',views.login_post,name="login_post"),
    path('admin_home/', views.admin_home, name="admin_home"),
    path('password/',views.admin_password,name="password"),
    path('admin_complaint/',views.admin_view_complaint,name="admin_complaint"),
    path('add_staff/',views.admin_add_staff,name="add_staff"),
    path('staff_post/',views.admin_staff_post,name="staff_post"),
    path('admin_donation/',views.admin_donation,name="admin_donation"),
    path('complaint_reply/',views.admin_complaint_reply,name="complaint_reply"),
    path('add_committee/',views.admin_add_committee,name="add_committee"),
    path('committee_post/',views.admin_committee_post,name="committee_post"),
    path('admin_report_view/',views.admin_report_view,name="admin_report_view"),
    path('committee_add_fund/',views.committee_add_fund,name="committee_fund"),
    path('committee_add_fund_post/',views.committee_add_fund,name="committee_fund"),
    path('committee_add_event/',views.committee_add_event,name="committee_add_event"),
    path('committee_event_post/',views.committe_event_post,name="committee_event_post"),
    path('committee_manage_events/',views.committee_manage_event,name="committe_event"),
    path('committee_event_report/',views.committee_event_report,name="committee_report"),
    path('staff_add_sermons/',views.staff_add_sermons,name="staff_add_sermons"),
    path('staff_sermons_post/',views.staff_add_sermons,name="staff_add_sermons"),
    path('staff_baptism/',views.staff_baptism,name="staff_baptism"),
    path('staff_confession/',views.staff_confession,name="staff_confession"),
    path('staff_marriage/',views.staff_marriage,name="staff_marriage"),
    path('staff_prayer/',views.staff_prayer,name="staff_prayer"),
    path('user_confession/',views.user_confession,name="user_confession"),
    path('user_marriage/',views.user_marriage,name="user_marriage"),
    path('user_prayer/',views.user_prayer,name="user_prayer"),
    path('user_donation/',views.user_donation,name="user_donation"),
    path('user_donation_post/',views.user_donation,name="user_doantion_post"),

]

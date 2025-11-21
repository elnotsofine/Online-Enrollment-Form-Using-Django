from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),

    path("student-data/", views.student_data, name="student_data"),
    path("personal-info/", views.personal_info, name="personal_info"),
    path("educational-bg/", views.educational_bg, name="educational_bg"),
    path("family-bg/", views.family_bg, name="family_bg"),
    path("schedule/", views.schedule, name="schedule"),

    path("logout/", views.logout_view, name="logout"),
]

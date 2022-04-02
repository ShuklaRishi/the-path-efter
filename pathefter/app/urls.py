from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.HomepageView.as_view()),
    path("signup/", views.SignupView.as_view()),
    path("guidesSignup/", views.GuideSignupView.as_view()),
    path("guideDashboard/", views.DashboardView.as_view()),
    path("login/", views.LoginView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path("profile/", views.ProfileView.as_view()),
    path("pie/", views.PieChartsView.as_view()),
    path("flowcharts/", views.FlowchartsView.as_view()),
    path("meets/", views.MeetsView.as_view()),
     path("scheduled/", views.ScheduledView.as_view()),
]

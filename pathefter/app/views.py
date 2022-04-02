from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .forms import SignUpForm
from django.contrib.auth.models import AnonymousUser
from datetime import datetime, timedelta
from .models import Meets

User = get_user_model()
# Create your views here.
class HomepageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "Home.html", context=None)


class LoginView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "Login.html", context=None)

    def post(self, request, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(to="/home/")
        return render(
            request, "Login.html", context={"msg": "Incorrect username or password"}
        )


class SignupView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "Signup.html", context=None)
      
    def post(self,request, **kwargs):
        data = request.POST.copy()
        data['date_joined'] = datetime.now()
        data['password'] = data['password1']
        data["is_active"] = True
        data["isStudent"] = True
        form = SignUpForm(data)
        if form.is_valid():
            print("YES")
            form.save()
            return redirect(to="/login/")
        print(form.errors)
        return render(request, "Signup.html", context={"msg": form.errors})  


class GuideSignupView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "guidesSingup.html", context=None)
    
    def post(self,request, **kwargs):
        data = request.POST.copy()
        data['date_joined'] = datetime.now()
        data['password'] = data['password1']
        data["is_active"] = True
        data["isStudent"] = False
        form = SignUpForm(data)
        print(form)
        if form.is_valid():
            print("YES")
            form.save()
            return redirect(to="/login/")
        return render(request, "Signup.html", context={"msg": form.errors}) 

class DashboardView(TemplateView):
    def get(self, request, **kwargs):
        if request.user.is_authenticated and not request.user.isStudent:
            week1=datetime.now().date()-timedelta(days=7)
            studMeets=Meets.objects.filter(meet__gte=week1).order_by("-meet")
            return render(request, "guideDashboard.html", context={"data":studMeets})
        return redirect(to="/login/")



class MeetsView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "meets.html", context=None)

    def post(self, request, **kwargs):
        if request.user:
            meet=Meets(student=request.user, meet=datetime.now())
            meet.save()     
        return redirect(to="/scheduled/")


class ScheduledView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "scheduled.html", context=None)



class LogoutView(TemplateView):
    def get(self, request, **kwargs):
        logout(request)
        return redirect(to="/login/")


class ProfileView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "profile.html", context={"user": request.user})

class PieChartsView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "pie.html", context=None)

class FlowchartsView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "flowcharts.html", context=None)
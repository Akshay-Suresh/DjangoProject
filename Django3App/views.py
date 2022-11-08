from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
from Django3App.forms import StudentForm, LoginForm, ParentForm


def home(request):
    return render(request, 'home.html')


def reg_view(request):
    return render(request, 'reg.html')




def Login_View(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_view')
            if user.is_Student:
                return redirect('student_view')
            if user.is_Parent:
                return redirect('parent_view')
    return render(request, 'login.html')













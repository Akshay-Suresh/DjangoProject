from django.shortcuts import render, redirect

from Django3App.forms import StudentForm, LoginForm
from Django3App.models import Attendance, Student, Food


def student_view(request):
    return render(request, 'student/student.html')


def Student_Reg_View(request):
    form_s = StudentForm()
    form_l = LoginForm()
    if request.method == 'POST':
        form_s = StudentForm(request.POST)
        form_l = LoginForm(request.POST)
        if form_s.is_valid() and form_l.is_valid():
            user = form_l.save(commit=False)
            user.is_Student = True
            user.save()
            user1 = form_s.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('Login_View')
    return render(request, 'student/reg.html', {'form_s': form_s, 'form_l': form_l})


def StudentAttendanceView(request):
    u = Student.objects.get(user=request.user)
    sat = Attendance.objects.filter(st=u)
    return render(request, 'student/StudentAttendanceView.html', {'sat':sat})


def StudentFoodView(request):
    fob = Food.objects.all()
    return render(request, 'student/StudentFoodView.html', {'fob':fob})
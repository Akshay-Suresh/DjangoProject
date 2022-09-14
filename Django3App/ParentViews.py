from django.shortcuts import render, redirect

from Django3App.forms import LoginForm, ParentForm
from Django3App.models import Student, Attendance, Parent


def parent_view(request):
    return render(request, 'parent/Parent.html')


def Parent_Reg_View(request):
    form_l = LoginForm()
    form_q = ParentForm()
    form_p = Student.objects.filter(category='Hostlers')
    print(form_p)
    if request.method == 'POST':
        form_l = LoginForm(request.POST)
        form_q = ParentForm(request.POST)
        if form_l.is_valid() and form_q.is_valid():
            user = form_l.save(commit=False)
            user.is_Parent = True
            user.save()
            user1 = form_p.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('Login_View')
    return render(request, 'parent/regParent.html', {'form_l':form_l, 'form_q':form_q, 'form_p':form_p})


def StudentAttendanceView_Parent(request):
    u = Parent.objects.get(user=request.user)
    psat = Attendance.objects.filter(st=u.student)
    return render(request, 'parent/StudentAttendanceView_Parent.html', {'psat':psat})
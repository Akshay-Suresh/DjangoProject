import datetime

from django.contrib import messages
from django.shortcuts import render, redirect

from Django3App.forms import FoodForm, RoomForm, AlotRoomForm, AlotRoomFilter
from Django3App.models import Student, Parent, Food, RoomDetails, LoginView, Attendance, AlotRoom


def admin_view(request):
    return render(request, 'admin/admin.html')


def View_Student(request):
    sob = Student.objects.all()
    return render(request, 'admin/ViewStudent.html', {'sob': sob})


def Delete_Student(request, id):
    data = Student.objects.get(id=id)
    d = LoginView.objects.get(student=data)
    if request.method == 'POST':
        d.delete()
        return redirect('View_Student')
    else:
        return redirect('View_Student')


def View_Parent(request):
    pob = Parent.objects.all()
    return render(request, 'admin/ViewParent.html', {'pob': pob})


def AddFood(request):
    form = FoodForm()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Food Added Successfully')
            return redirect('Viewfood')
    return render(request, 'admin/Addfood.html', {'form':form})


def ViewFood(request):
    fob = Food.objects.all()
    return render(request, 'admin/Viewfood.html', {'fob':fob})


def DeleteFood(request, id):
    data = Food.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('Viewfood')
    else:
        return redirect('Viewfood')


def Room_Add(request):
    rform = RoomForm()
    if request.method == 'POST':
        rform = RoomForm(request.POST)
        if rform.is_valid():
            rform.save()
            return redirect('Room_View')
    return render(request, 'admin/AddRoom.html', {'rform':rform})


def Room_View(request):
    rob = RoomDetails.objects.all()
    return render(request, 'admin/ViewRoom.html', {'rob':rob})


def AddAttendance(request):
    s = Student.objects.all()
    return render(request, 'admin/AddAttendance.html', {'s':s})



now = datetime.datetime.now()


def mark(request, id):
    user = Student.objects.get(id=id)
    att = Attendance.objects.filter(st=user, date=datetime.date.today())
    if att.exists():
        messages.info(request, "Today's Attendance Already marked for this Student ")
        return redirect('AddAttendance')
    else:
        if request.method == 'POST':
            attndc = request.POST.get('attend')
            print(attndc)
            Attendance(st=user, date=datetime.date.today(), attend=attndc, time=now.time()).save()
            print(Attendance)
            messages.info(request, "Attendance Added successfully ")
            return redirect('AddAttendance')
    return render(request, 'admin/MarkAttendance.html', {'Attendance': Attendance})


def ViewAttendancePresent(request):
    atP = Attendance.objects.filter(attend='Present')
    return render(request, 'admin/ViewAttendancePresent.html', {'atP':atP})


def ViewAttendanceAbsent(request):
    atA = Attendance.objects.filter(attend='Absent')
    return render(request, 'admin/ViewAttendanceAbsent.html', {'atA':atA})


def view_attendance(request):
    value_list = Attendance.objects.values_list('date', flat=True).distinct()
    attendance = {}
    for value in value_list:
        attendance[value] = Attendance.objects.filter(date=value)
    return render(request, 'admin/view_attendance.html', {'attendances': attendance})


def day_attendance(request, date):
    attendance = Attendance.objects.filter(date=date)
    context = {
        'attendances': attendance,
        'date': date
    }
    return render(request, 'admin/day_attendance.html', context)


def AlotRoom_View(request):
    aform = AlotRoomForm()
    if request.method == 'POST':
        aform = AlotRoomForm(request.POST)
        if aform.is_valid():
            aform.save()
            return redirect('Alot_Room')
    return render(request, 'admin/AlotRoom.html', {'aform': aform})


def ViewAlotRoom(request):
    retrieve = AlotRoom.objects.all()
    f = AlotRoomFilter(request.GET, queryset=retrieve)
    # retrieve = f.qs
    return render(request, 'admin/ViewAlotRoom.html', {'retrieve':retrieve, 'filter':f})




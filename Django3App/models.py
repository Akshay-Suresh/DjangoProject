from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class LoginView(AbstractUser):
    is_Student = models.BooleanField(default=False)
    is_Parent = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(LoginView, on_delete=models.CASCADE, related_name='student')
    name = models.CharField(max_length=50)
    reg = models.CharField(max_length=50)
    email = models.EmailField()
    ph = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.reg


class Parent(models.Model):
    user = models.OneToOneField(LoginView, on_delete=models.CASCADE, related_name='parent')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    stat = (('Father', 'Father'), ('Mother', 'Mother '), ('Guardian', 'Guardian'))
    status = models.CharField(max_length=50, choices=stat, default='parent', null=True)
    email = models.EmailField()
    ph = models.CharField(max_length=50)

    # def __str__(self):
    #     return "%s" % self.name


# class RegParentModel(models.Model):
#     name1 = models.CharField(max_length=30)
#     email1 = models.EmailField()
#     phone1 = models.CharField(max_length=10)
#     relation1 = models.CharField(max_length=10)


class Food(models.Model):
    breakfast = models.CharField(max_length=50)
    btime = models.TimeField()
    lunch = models.CharField(max_length=50)
    ltime = models.TimeField()
    dinner = models.CharField(max_length=50)
    dtime = models.TimeField()


class RoomDetails(models.Model):
    total = models.IntegerField()
    avail = models.IntegerField()
    occupied = models.IntegerField()


class Attendance(models.Model):
    st = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    attend = models.CharField(max_length=50)
    time = models.TimeField()

    # def __str__(self):
    #     return "%s" % self.st


class AlotRoom(models.Model):
    stu = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='alotroom')
    roomno = models.CharField(max_length=50)
    roommates = models.CharField(max_length=150)
    img = models.FileField(upload_to="documents/")






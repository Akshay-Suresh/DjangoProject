import django_filters
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_filters import CharFilter

from Django3App.models import LoginView, Student, Parent, Food, RoomDetails, AlotRoom


class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )

    class Meta:
        model = LoginView
        fields = ('username', 'password1', 'password2')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'reg', 'category', 'email', 'ph')


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ('student',)


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


class RoomForm(forms.ModelForm):
    class Meta:
        model = RoomDetails
        fields = '__all__'


class AlotRoomForm(forms.ModelForm):
    class Meta:
        model = AlotRoom
        fields = '__all__'


class AlotRoomFilter(django_filters.FilterSet):
    stu = CharFilter(field_name='stu', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = AlotRoom
        fields = ('stu',)




import django_filters
from django import forms
from django_filters import CharFilter

from Django3App.forms import AlotRoomForm
from Django3App.models import AlotRoom, Student


class AlotRoomFilter(django_filters.FilterSet):
    roomno = CharFilter(field_name='roomno', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Search RoomNo.', 'class': 'form-control'}))

    class Meta:
        model = AlotRoom
        fields = ('roomno',)


class StudentFilter(django_filters.FilterSet):
    reg = CharFilter(field_name='reg', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Search Register No.', 'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ('reg',)
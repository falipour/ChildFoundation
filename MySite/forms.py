import django
from django import forms
from MySite.models import *


# TODO
# class ComplexForm(django.forms.ModelForm):
#     class Meta:
#         model = Complex
#         fields = ['name', 'address', 'unit_number']
#
#
# class NewsForm(django.forms.ModelForm):
#     class Meta:
#         model = News
#         exclude = ['date']
#
#
# class EventForm(django.forms.ModelForm):
#     class Meta:
#         model = Event
#         exclude = ['date']
#
#
#
# class DisplayForm(django.forms.Form):
#     startDate = django.forms.DateField()
#     finishDate = django.forms.DateField()

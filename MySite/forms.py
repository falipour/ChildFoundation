from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)
    title = forms.CharField(max_length=200, required=True)
    text = forms.CharField(max_length=1000, required=True)

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'title', 'text', ]

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "نام و نام خانوادگی"
        self.fields['email'].label = "پست الکترونیکی"
        self.fields['title'].label = "عنوان"
        self.fields['text'].label = "متن"
        self.fields['name'].widget.attrs[
            'style'] = 'width:400px; height:20px; border-radius=5px; direction:rtl; float:left;'
        self.fields['email'].widget.attrs['style'] = 'width:400px; height:20px; border-radius=5px; float:left;'
        self.fields['title'].widget.attrs[
            'style'] = 'width:400px; height:20px; border-radius=5px; direction:rtl; float:left;'
        self.fields['text'].widget.attrs[
            'style'] = 'width:400px; height20px; border-radius=5px; direction:rtl; float:left;'

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

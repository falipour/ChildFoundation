from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "نام"
        self.fields['last_name'].label = "نام خانوادگی"
        self.fields['email'].label = "پست الکترونیکی"
        self.fields['password'].label = "رمز عبور"
        self.fields['username'].label = "نام کاربری"

        self.fields['first_name'].widget.attrs[
            'style'] = 'width:70%; height:18px; border-radius=5px; direction:rtl; float:left;'
        self.fields['email'].widget.attrs[
            'style'] = 'width:70%; height:18px; border-radius=5px; direction:rtl; float:left;'
        self.fields['last_name'].widget.attrs[
            'style'] = 'width:70%; height:18px; border-radius=5px; direction:rtl; float:left;'
        self.fields['password'].widget.attrs[
            'style'] = 'width:70%; height:18px; border-radius=5px; direction:rtl; float:left;'
        self.fields['username'].widget.attrs[
            'style'] = 'width:70%; height:18px; border-radius=5px; direction:rtl; float:left;'

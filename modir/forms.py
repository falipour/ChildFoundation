from django import forms
from madadkar.models import Madadkar

FIELD_NAME_MAPPING = {
    'username': 'نام کاربری',
    'password': 'رمز عبور'
}


# class MadadkarForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = Madadkar
#         fields = ['username', 'email', 'password', 'national_id', 'country', 'city', 'address', 'postal_code',
#                   'phone_number']
#         labels = {'username': 'نام کاربری',
#                   'email': 'ایمیل',
#                   'password': 'رمز عبور',
#                   'national_id': 'کد ملی',
#                   'country': 'کشور',
#                   'city': 'شهر',
#                   'address': 'آدرس',
#                   'postal_code': 'کد پستی',
#                   'phone_number': 'شماره تلفن',
#                   }

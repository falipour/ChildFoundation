from django import forms
from .models import Hamyar


class HamyarForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Hamyar
        fields = ['country', 'city', 'address',
                  'postal_code', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(HamyarForm, self).__init__(*args, **kwargs)
        # self.fields['first_name'].label = "نام"
        # self.fields['last_name'].label = "نام خانوادگی"
        # self.fields['email'].label = "پست الکترونیکی"
        # self.fields['password'].label = "رمز عبور"
        # self.fields['national_id'].label = "کد ملی"
        # self.fields['country'].label = "کشور"
        # self.fields['city'].label = 'شهر'
        # self.fields['address'].label = 'آدرس'
        # self.fields['postal_code'].label = 'کد پستی'
        # self.fields['phone_number'].label = 'شماره تلفن'

        # self.fields['first_name'].widget.attrs[
        #     'style'] = 'width:400px; height:20px; border-radius=5px; direction:rtl; float:left;'
        # self.fields['email'].widget.attrs['style'] = 'width:400px; height:20px; border-radius=5px; float:left;'
        # self.fields['last_name'].widget.attrs[
        #     'style'] = 'width:400px; height:20px; border-radius=5px; direction:rtl; float:left;'
        # self.fields['country'].widget.attrs[
        #     'style'] = 'width:400px; height20px; border-radius=5px; direction:rtl; float:left;'

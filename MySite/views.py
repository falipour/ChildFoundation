from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.core.mail import mail_admins, send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    # TODO
    # if request.method == 'POST':
    #     if request.POST.get('submit') == 'ورود':
    #         return login(request)
    #     elif request.POST.get('submit') == 'ثبت نام':
    #         return signup(request)
    #     elif request.POST.get('submit') == 'ثبت نام مجتمع':
    #         return complexRegister(request)
    #     else:
    #         return forget_password(request)
    return render(request, 'MySite/Home.html')


def chart(request):
    # TODO
    # if request.method == 'POST':
    #     if request.POST.get('submit') == 'ورود':
    #         return login(request)
    #     elif request.POST.get('submit') == 'ثبت نام':
    #         return signup(request)
    #     elif request.POST.get('submit') == 'ثبت نام مجتمع':
    #         return complexRegister(request)
    #     else:
    #         return forget_password(request)
    return render(request, 'MySite/Chart.html')
from django.shortcuts import render, redirect
from django.views import View
from .forms import MadadkarForm
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView


class AdminGoalsView(TemplateView):
    template_name = 'modir/Admin_Goals.html'


class AdminHomeView(TemplateView):
    template_name = 'modir/Admin_Home.html'


class AdminContactView(TemplateView):
    template_name = 'modir/Admin_Contact.html'


class AdminHistoryView(TemplateView):
    template_name = 'modir/Admin_History.html'


class AdminChartView(TemplateView):
    template_name = 'modir/Admin_Chart.html'


class AdminMadadkarRegisterView(View):
    form_class = MadadkarForm
    template_name = 'modir/Madadkar_Register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


class UserFormView(View):
    form_class = MadadkarForm
    template_name = 'music/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('modir:admin-home')
        return render(request, self.template_name, {'form': form})



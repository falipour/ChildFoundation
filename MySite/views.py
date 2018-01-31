from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import ContactForm


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


def goals(request):
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
    return render(request, 'MySite/Goals.html')


def history(request):
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
    return render(request, 'MySite/History.html')


def contact(request):
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

    return render(request, 'MySite/Contact.html')


class ContactView(TemplateView):
    template_name = 'MySite/Contact.html'

    def get(self, request, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        text = None
        if form.is_valid():
            # post = form.save(commit=False)
            # post.user = request.user
            # post.save()
            form.save()
            text = form.cleaned_data
            form = ContactForm()

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

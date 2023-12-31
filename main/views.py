from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect

from main.form import MessagesForm
from main.helpers import GetContext

from mailing.mail import Mail
from dbcore.models import Feedback


class FeedbackView(View):
    def post(self, request, *args, **kwargs):
        if not request.recaptcha_is_valid:
            _mutable = request.GET._mutable
            request.GET._mutable = True
            request.GET['recaptcha'] = False
            request.GET._mutable = _mutable
            return redirect('main:invalid_feedback', lang=kwargs.get('lang'))
        
        form = MessagesForm(request.POST, request.FILES, kwargs)
        if form.is_valid():
            fio = form.cleaned_data.get('fio')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('comment')

            feedback = Feedback(
                fio=fio,
                phone=phone,
                email=email,
                text=text
            )
            feedback.save()

            Mail(feedback)()

        if kwargs.get('lang') in ('ru', 'eng'):
            return redirect('main:page_with_lang', lang=kwargs.get('lang'))
        
        return redirect('main:main_page')
    

class MainPage(View):
    def get(self, request, *args, **kwargs):
        context = GetContext(lang='kz')()
        context['form'] = MessagesForm(lang='kz')
        context['captcha_link'] = 'https://www.google.com/recaptcha/api.js?explicit&hl=en'
        
        return render(request, 'main.html', context)
    

class Page(View):
    def get(self, request, *args, **kwargs):
        context = GetContext(lang=kwargs.get('lang'))()
        context['form'] = MessagesForm(lang=kwargs.get('lang'))
        context['captcha_link'] = 'https://www.google.com/recaptcha/api.js?explicit&hl=en'
        
        return render(request, 'main.html', context)
    

class InvalidCaptchaToFeedback(View):
    def get(self, request, *args, **kwargs):
        context = GetContext(lang=kwargs.get('lang'))()
        context['form'] = MessagesForm(lang=kwargs.get('lang'))
        context['captcha_link'] = 'https://www.google.com/recaptcha/api.js?explicit&hl=en'
        context['invalid_recaptcha'] = True

        return render(request, 'main.html', context)



        

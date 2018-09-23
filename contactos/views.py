from django.core.mail import send_mail
from django.shortcuts import render

from __LRS_Propiedades__ import settings
from .forms import contactForm

def contacto(request):
    title = 'Contact'
    viewContactForm = contactForm(request.POST or None)
    context = {'title': title, 'form': viewContactForm, }

    if viewContactForm.is_valid():
        name = viewContactForm.cleaned_data['name']
        comment = viewContactForm.cleaned_data['comment']

        subject = 'Message From mysite'
        message = '%s %s' %(comment, name)
        emailFrom = viewContactForm.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(
            subject,
            message,
            emailFrom,
            emailTo,
            fail_silently=False,
        )
        title = "Gracias!"
        confirm_message = "Gracias por el mensaje, estaremos en contacto"
        context = {'title': title, 'confirm_message': confirm_message, }

    #context = locals()
    template = 'contacto.html'
    return render(request, template, context)
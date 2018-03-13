from django.shortcuts import render
from . import forms
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse
# from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def hello_world(request):
    return render(request, 'home.html')


def contact_us_view(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            print("good form")

            mail_subject = 'Activate your Lead Shop account.'
            # current_site = get_current_site(request)
            # message = render_to_string('')
            message = 'HELLO'
            # 'user': user,
            # 'domain': current_site.domain,
            # 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            # 'token': account_activation_token.make_token(user),
            # })
            email = EmailMessage(mail_subject, message, from_email='leadshop@motorhubmagazine.com', to=['abahoalvin@gmail.com'])
            email.send()
            # send_mail(
            #     'Contact from {}'.format(form.cleaned_data['name']),
            #     form.cleaned_data['message'],
            #     '{name} <{email}>'.format(**form.cleaned_data),
            #     # ['abahoalvin@gmail.com']
            # )
            messages.add_message(request, messages.SUCCESS,
                                 'Thank you for contacting us')
            return HttpResponseRedirect(reverse('contact_us'))

    return render(request, 'contact_us_form.html', {'form': form})

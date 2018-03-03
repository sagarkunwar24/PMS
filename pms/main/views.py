from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django import forms
from django.contrib.auth.decorators import login_required
from .forms import PurchaseOrderForm

@login_required
def home(request):
    return render(request, 'main/home.html')

@login_required
def email(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PurchaseOrderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            send_mail(
                'SUBJECT',
                'Hi Bob, here is a message.',
                'yee.camero23@gmail.com',
                ['yee.camero23@gmail.com'],
                fail_silently=False,
            )

            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PurchaseOrderForm()

    return render(request, 'main/email.html', {'form': form})

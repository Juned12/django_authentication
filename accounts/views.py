from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

#local file import goes below
from .models import User
from .forms import SignUpForm
from .utils import send_html_mail 

@login_required
def index(request):
    return render(request, 'index.html')

def register(request):
    context = {}
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'index.html')
    context['form'] = form
    return render(request, 'registration/register.html', context)

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):  
    if created:
        recipient_list = [instance.email]
        subject = "Welcome to Django"  
        html_template = 'accounts/email/welcome_email.html'
        html_content = render_to_string(html_template, {})
        send_html_mail(subject, html_content, recipient_list)


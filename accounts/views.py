from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import RegisterForm
from time import sleep
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from datetime import datetime
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
def login_view(request):
    login_form = AuthenticationForm()
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, "Hurmatli foydalanuvchi, siz hisobingizga muvaffaqiyatli kirdingiz !...")
            return redirect("home")
        else:
            messages.warning(request, "Hurmatli foydalanuvchi formani to'g'ri ma'lumotlar bilan to'ldiring !...")
            return render(request, "registration/login.html", {"form": login_form})
    else:
        return render(request, "registration/login.html", {"form": login_form})

def logout_view(request):
    logout(request)
    messages.success(request, "Hurmatli foydalanuvchi, siz hisobingizdan muvaffaqiyatli chiqdingiz !...")
    return redirect("login")

def profile(request):
    if request.user.is_authenticated:
        return render(request, "accounts/profile.html")
    else:
        return redirect("home")
    
def user_register(request):
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.set_password(
                register_form.cleaned_data['password']
            )
            user.save()
            messages.info(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz !")


            today = datetime.now()
            year = today.strftime("%Y")
            my_subject = "Tabriklaymiz, siz ro'yxatdan o'tdingiz."
            receiver_email = register_form.cleaned_data['email']
            current_site = get_current_site(request)
            email_context = {
                "year": year,
                "user": user,
                "site_name": current_site.name
            }

            html_message = render_to_string("content/email.html", context=email_context)
            plain_message = strip_tags(html_message)

            message = EmailMultiAlternatives(
                subject=my_subject,
                body=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                to=[receiver_email]
            )
            message.attach_alternative(html_message, "text/html")
            message.send()

            login(request, user)
            messages.info(request, "Siz muvaffaqiyatli hisobingizga kirdingiz !")
            context = {
                    "form": register_form
                }
            return redirect("home")
        else:
            context = {
                    "form": register_form
                }
            return render(request, "accounts/register.html", context)
    else:
        context = {
        "form": register_form
        }
        return render(request, "accounts/register.html", context)
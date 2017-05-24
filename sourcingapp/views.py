from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from sourcingapp.forms import SignUpForm
from random import randint
from django.views.generic import TemplateView
#Added for signup email confirmation
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from sourcingapp.tokens import account_activation_token


# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")

# Basic sign up page
#/signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            #user.refresh_from_db()  # load the profile instance created by the signal
            #user.profile.company = form.cleaned_data.get('company')
            user.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=user.username, password=raw_password)
            #login(request, user)
            #return redirect('home')
            current_site = get_current_site(request)
            subject = 'Activate Your Hire99 Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Signup email confirmation
def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

# Signup activation
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


def base(request):
    return render(request,"base.html")

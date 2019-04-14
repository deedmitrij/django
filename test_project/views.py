from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .forms import UserForm, RecoveryForm, UserProfileForm, UserChangePassForm
from django.shortcuts import render
import time



def signup(request):
    form = UserForm(request.POST or None)
    # request.is_ajax()
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'],
                                        first_name=data['first_name'], last_name=data['last_name'])
        message = 'Your data has been accepted. Wait while redirected to the login page...'
        time.sleep(3)
        return HttpResponseRedirect('/')

    if request.is_ajax():
        return HttpResponse("OK")
    else:
        return render(request, 'registration/signup.html', locals())


def pass_recovery(request):
    # form = RecoveryForm(request.POST)
    return render(request, 'registration/pass_recovery.html', locals())


def measurement(request):
    return render(request, 'user_weight.html')


def user_profile(request):
    user = User.objects.get(username=request.user.username)
    data = user.__dict__
    info_form = UserProfileForm(initial=data) if request.method == 'GET' else UserProfileForm(request.POST, instance=user)
    pass_form = UserChangePassForm(request.POST or None)
    if request.method == 'POST' and info_form.is_valid():
        user.username = info_form.cleaned_data['username']
        user.save()
    elif request.method == 'POST' and pass_form.is_valid():
        if user.check_password(pass_form['old_pass'].data):
            if pass_form['new_pass'].data == pass_form['repeat_pass'].data:
                user.set_password(pass_form['new_pass'].data)
                user.save()
                return HttpResponse("OK")
    return render(request, 'user_profile.html', locals())

# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world!. You're at the Django test project.")

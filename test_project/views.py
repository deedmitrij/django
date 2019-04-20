from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .forms import UserForm, RecoveryForm, UserProfileForm, UserChangePassForm
from django.shortcuts import render
import time


def signup(request):
    # form = UserForm(request.POST or None)
    if request.method == 'GET':
        return HttpResponseRedirect('/')
    # elif request.method == 'POST' and form.is_valid():
    elif request.method == 'POST' and request.is_ajax():
        # data = form.cleaned_data
        if User.objects.filter(username=request.POST['username']).exists():
            return HttpResponse("username is exist")
        elif User.objects.filter(email=request.POST['email']).exists():
            return HttpResponse("email is exist")
        else:
            User.objects.create_user(username=request.POST['username'], email=request.POST['email'],
                                     password=request.POST['password'], first_name=request.POST['first_name'],
                                     last_name=request.POST['last_name'])
    #     message = 'Your data has been accepted. Wait while redirected to the login page...'
    #     time.sleep(3)
    #     return HttpResponseRedirect('/')
            return HttpResponse("OK")
    # else:
    #     return render(request, 'registration/signup.html', locals())
    else:
        return HttpResponse("Non-valid request")


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
        user.first_name = info_form.cleaned_data['first_name']
        user.last_name = info_form.cleaned_data['last_name']
        user.email = info_form.cleaned_data['email']
        user.save()
    elif request.method == 'POST' and request.is_ajax():
        if user.check_password(request.POST['old_pass']):
            user.set_password(request.POST['new_pass'])
            user.save()
            return HttpResponse("OK")
        else:
            return HttpResponse("Incorrect password")
    return render(request, 'user_profile.html', locals())

# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world!. You're at the Django test project.")

from django.http import HttpResponseRedirect
from .forms import UserForm
from django.shortcuts import render
import time



def signup(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form = form.save()
        message = 'Your data has been accepted. Wait while redirected to the login page...'
        time.sleep(3)
        return HttpResponseRedirect('/')
    return render(request, 'registration/signup.html', locals())


def measurement(request):
    return render(request, 'user_weight.html')


# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world!. You're at the Django test project.")

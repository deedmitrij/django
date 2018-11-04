from django.shortcuts import render
from .models import Measurement, Participant


# Create your views here.


def measurement(request):
    user = Participant.objects.name()
    # measure_list = Measurement.objects.filter()
    return render(request, 'user_weight.html', user)

# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world!. You're at the Django test project.")

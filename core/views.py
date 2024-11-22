import random

from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html', {})


def color(request):
    color = "%06x" % random.randint(0, 0xFFFFFF)
    return render(request, 'core/color.html', {'color': color})

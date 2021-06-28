from django.shortcuts import render
from .models import Turf
from .forms import TurfCreateForm

# Create your views here.

def turf_list(request):
    turfs = Turf.objects.all()
    content = {
        'turfs' : turfs
    }
    return render(request, 'turf/turf_list.html', content)

def add_turf(request):
    form = TurfCreateForm()
    content = {
        'form' : form
    }
    return render(request, 'turf/turf_list.html', content)

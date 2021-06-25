from django.shortcuts import render
from .models import Turf
# Create your views here.

def turf_list(request):
    turfs = Turf.objects.all()
    content = {
        'turfs' : turfs
    }
    return render(request, 'turf/turf_list.html', content)

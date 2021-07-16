from django.shortcuts import render
from .models import Turf
from .forms import TurfCreateForm
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    if request.user.is_authenticated:
        admin = False
        if request.user.profile.is_admin:
            admin = True
            return render(request, 'turf/index.html', {'admin' : admin})
        else:
            return render(request, 'turf/index.html', {'admin' : admin})
    turfs = Turf.objects.all()
    content = {
        'turfs':turfs,
    }

    return render(request, 'turf/index.html', content)

@login_required
def search_turf(request):
    user = request.user
    fav = bool
    l = []
    if user.profile.is_admin:
        messages.warning(request,"You need a customer account")
    else:
        if request.method == 'GET':    
            place =  request.GET.get('place')
            category = request.GET.get('category')
            object_list = Turf.objects.filter(Q(place__icontains=place))
        user_fav = Turf.objects.user_favourites(user)
        return render(request, 'turfs/search_result.html', {'object':object_list, 'fav':user_fav})
    return render(request, 'turfs/search_result.html')

def turf_list(request):
    turfs = Turf.objects.all()
    content = {
        'turfs' : turfs
    }
    return render(request, 'turf/turf_list.html', content)



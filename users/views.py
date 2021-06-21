from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, UserProfileForm, VendorLoginForm

# Create your views here

def admin_register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        p_form = UserProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            new_user = u_form.save()
            profile = p_form.save(commit=False)
            if profile.user_id is None:
                profile.user_id = new_user.id
            profile.save()
            messages.success(request,f'profile created')
            return redirect('login')
    else:
        u_form = UserRegisterForm()
        p_form = UserProfileForm()

    content = {
        'u_form':u_form,
        'p_form':p_form,
    }

    return render(request, 'users/admin_register.html',content)

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        account = authenticate(username=username, password=password)
        if account is not None:
            if account.profile.is_admin:
                login(request, account)
                return redirect('/')
            messages.warning(request,f'username or password is incorrect')
        else:
            messages.warning(request,f'username or password is incorrect')
    
    form = VendorLoginForm()

    context = {'form':form}

    return render(request, 'users/admin_login.html', context)
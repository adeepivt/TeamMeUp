from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, UserProfileForm, UserLoginForm
from turf.forms import TurfCreateForm
from django.contrib.auth.decorators import login_required


def admin_register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        p_form = UserProfileForm(request.POST, request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            new_user = u_form.save()
            profile = p_form.save(commit=False)
            if profile.user_id is None:
                profile.user_id = new_user.id
                profile.is_admin = True
                profile.save()
            messages.success(request,f'profile created')
            return redirect('/')
    else:
        u_form = UserRegisterForm()
        p_form = UserProfileForm()

    content = {
        'u_form':u_form,
        'p_form':p_form,
    }

    return render(request, 'users/register.html',content)

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        account = authenticate(username=username, password=password)
        if account is not None:
            if account.profile.is_admin:
                login(request, account)
                return redirect('admin_home')
            messages.warning(request,f'username or password is incorrect')
        else:
            messages.warning(request,f'username or password is incorrect')
    
    form = UserLoginForm()

    context = {'form':form}

    return render(request, 'users/login.html', context)

@login_required
def admin_home(request):
    if request.method == 'POST':
        form = TurfCreateForm(request.POST)
        managerForm = UserRegisterForm(request.POST)
        if form.is_valid() and managerForm.is_valid():
            m = managerForm.save()
            instance = form.save(commit=False)
            instance.owner = request.user
            if instance.manager_id is None:
                instance.manager_id = m.id
                instance.save()
                return redirect('home')
    else:
        form = TurfCreateForm()
        managerForm = UserRegisterForm()
    content = {
        'form' : form,
        'managerForm' : managerForm
    }
    return render(request, 'users/admin_home.html', content)

def user_register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        p_form = UserProfileForm(request.POST, request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            new_user = u_form.save()
            profile = p_form.save(commit=False)
            if profile.user_id is None:
                profile.user_id = new_user.id
            profile.save()
            messages.success(request,f'profile created')
            return redirect('/')
    else:
        u_form = UserRegisterForm()
        p_form = UserProfileForm()

    content = {
        'u_form':u_form,
        'p_form':p_form,
    }

    return render(request, 'users/register.html',content)

def user_login(request):
    if request.method == 'POST':
        valuenext= request.POST.get('next')
        username = request.POST['username']
        password = request.POST['password']
        account = authenticate(username=username, password=password)
        if account is not None:
            if account.profile.is_admin:
                    messages.warning(request,f'username or password is incorrect')
            else:
                if valuenext == '':
                    login(request, account)
                    return redirect('/')
                else:
                    login(request, account)
                    return redirect(valuenext)
        else:
            messages.warning(request,f'username or password is incorrect')
    
    form = UserLoginForm()

    context = {'form':form}

    return render(request, 'users/login.html', context)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import ClientLoginForm

@login_required
def user_profile_view(request):
    return render(request, 'custom_user/user_profile.html')

def user_login_view(request):
    if request.method == 'POST':
        form = ClientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = ClientLoginForm()
    return render(request, 'custom_user/client_login.html', {'form': form})

@login_required
def user_logout_view(request):
    logout(request)
    return redirect('user_login')


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            return redirect('posts_app:success_stories')
        
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts_app/register.html', context)


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            # return redirect('app_name:success_stories')
            
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts_app/login.html', context)

def log_out(request):
    if request.method == 'POST':
        logout(request)
        # return redirect('main_app:home')
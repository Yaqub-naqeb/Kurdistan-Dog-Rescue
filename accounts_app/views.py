from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .form import RegisterUserForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # clean the data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log the user in
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Successful!'))
            return redirect('success_stories')
        
    else:
        form = RegisterUserForm()
        messages.success(request, ("There was an error logging in, please try again."))
    context = {'form': form}
    return render(request, 'accounts_app/register.html', context)


def log_in(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There was an error logging in, please try again."))
            return redirect('login')
            
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts_app/login.html', context)

def log_out(request):
    logout(request)
    messages.success(request, ("You were logged out."))
    return redirect('home')
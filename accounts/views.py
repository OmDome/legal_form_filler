from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse

# Registration Page
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Login Page
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')

# Logout
def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('home')  # Redirects to the homepage after logout

# Home
def home(request):
    return render(request, 'home.html')

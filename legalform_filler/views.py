from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from accounts.models import FormTemplate, FormField, UserResponse


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

# Home
def home(request):
    return render(request, 'home.html')

# Form Fill
def form_fill(request, form_id):
    # For now, we’ll just return a simple page with the form name based on form_id
    form_name = "FL-100 Petition - Marriage/Domestic Partnership" if form_id == 100 else "Unknown Form"
    return render(request, 'form_fill.html', {'form_name': form_name})

def fill_form_step(request, form_code, step_number):
    form_template = get_object_or_404(FormTemplate, form_code=form_code)
    fields = FormField.objects.filter(form_template=form_template, step_number=step_number)

    if request.method == 'POST':
        # Save responses
        for field in fields:
            response = request.POST.get(field.field_name)
            UserResponse.objects.update_or_create(
                user=request.user,
                form_template=form_template,
                field_name=field.field_name,
                defaults={'response': response or "off"}  # Save "off" if not checked
            )
        # Redirect to the next step or completion page
        next_step = step_number + 1
        if FormField.objects.filter(form_template=form_template, step_number=next_step).exists():
            return redirect('fill_form_step', form_code=form_code, step_number=next_step)
        else:
            return redirect('form_complete', form_code=form_code)

    return render(request, 'form_step.html', {'form_template': form_template, 'fields': fields, 'step_number': step_number})

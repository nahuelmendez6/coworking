from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import OwnerRegistratrionForm, CustomerRegistrationForm
from django.contrib import auth
from django.contrib.auth.models import Group
from django.contrib.auth import login

# Create your views here.
@login_required
def home_view(request):
    # Get user's groups
    user = request.user
    if user.groups.filter(name='owner').exists():
        # Redirect to the owner's template
        return render(request, 'home_owner.html', {'user':user})
    elif user.groups.filter(name='customer').exists():
        # Redirect to the customer's template
        return render(request, 'customer_home.html', {'user':user})


def register_customer(request):

    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            group.user_set.add(user)
            login(request, user)
            return redirect('home_view')
    else:
        form = CustomerRegistrationForm()

    return render(request, 'register_customer.html', {'form':form})


def register_owner(request):

    if request.method == 'POST':
        form = OwnerRegistratrionForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='owner')
            group.user_set.add(user)
            login(request, user)
            return redirect('home_view')

    else:
        form = OwnerRegistratrionForm()

    return render(request, 'register_owner.html', {'form':form})

def login(request):
    form = AuthenticationForm(request, request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home_view')

    return render(request, 'login.html', {'form':form})

def logout(request):
    login(request)
    return redirect('login')
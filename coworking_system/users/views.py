from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import OwnerRegistratrionForm, CustomerRegistrationForm
from django.contrib import auth
from django.contrib.auth.models import Group
from django.contrib.auth import login

# Create your views here.

def register_customer(request):

    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            group.user_set.add(user)
            login(request, user)
            return redirect('home')
    else:
        form = CustomerRegistrationForm()

    return render(request, 'register_customer.html', {'form':form})


def register_provier(request):

    if request.method == 'POST':
        form = OwnerRegistratrionForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='owner')
            group.user_set.add(user)
            login(request, user)
            return redirect('home')

    else:
        form = OwnerRegistratrionForm()

    return render(request, 'register_owner.html', {'form':form})


from django.shortcuts import render, redirect
from .models import Space, SpaceAddress
from .forms import NewSpaceForm
# Create your views here.
"""
En la gestion de de espacios, la primera view debe ser la que permita crear espacios nuevos
"""
def new_space(request):
    if request.method == 'POST':
        form = NewSpaceForm(request.POST)
        if form.is_valid():
            # Crear direccion
            address = SpaceAddress.objects.create(
                street = form.cleaned_data['street'],
                steet_number = form.cleaned_data['street_number'],
                floor = form.cleaned_data['floor'],
                apartment = form.cleaned_data['apartment'],
                reference = form.cleaned_data['reference'],
                city = form.cleaned_data['city'],
                deparpasstment = form.cleaned_data['department'],
                province = form.cleaned_data['province']
            )

            # Crear espacio
            space = form.save(commit=False)
            space.address = address
            space.owner = request.user
            space.save()

            return redirect('home')
    else:
        form = NewSpaceForm()
        return render(request, 'add_space.html', {'form':form})

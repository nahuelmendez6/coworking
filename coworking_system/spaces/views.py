from django.core.files import File
from django.shortcuts import render, redirect
from .models import Space, SpaceAddress, Amenity, Room
from .forms import NewSpaceForm, RoomFormSet, AmenityFormSet

# Create your views here.
"""
En la gestion de de espacios, la primera view debe ser la que permita crear espacios nuevos
"""
def new_space(request):
    if request.method == 'POST':
        form = NewSpaceForm(request.POST)
        room_formset = RoomFormSet(request.POST, prefix='rooms')
        amenity_formset = AmenityFormSet(request.POST, prefix='amenities')
        if form.is_valid():
            # Crear direccion
            address = SpaceAddress.objects.create(
                street = form.cleaned_data['street'],
                street_number = form.cleaned_data['street_number'],
                floor = form.cleaned_data['floor'],
                apartment = form.cleaned_data['apartment'],
                reference = form.cleaned_data['reference'],
                city = form.cleaned_data['city'],
                department = form.cleaned_data['department'],
                province = form.cleaned_data['province']
            )

            # Crear espacio
            space = form.save(commit=False)
            space.address = address
            space.owner = request.user
            space.save()

            # Guarda habitaciones relacionadas
            rooms = room_formset.save(commit=False)
            for room in rooms:
                room.space = space
                room.save()

            # Guarda las amenities relacionadas
            amenities = amenity_formset.save(commit=False)
            for amenity in amenities:
                amenity.space = space
                amenity.save()

            # Imagenes
            files = request.FILES.getlist('files')
            for file in files:
                File.objets.create(space=space, file=file)

            return redirect('home_view')

        else:
            # Si el formulario no es valido, lo renderiza con errores
            return render(request, 'add_space.html', {'form':form})
    else:
        form = NewSpaceForm()
        room_formset = RoomFormSet(prefix='rooms')
        amenity_formset = AmenityFormSet(prefix='amenities')

        return render(request, 'add_space.html',
                      {
                          'form': form,
                          'room_formset': room_formset,
                          'amenity_formset': amenity_formset,
                      })


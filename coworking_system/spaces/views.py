from django.core.files import File
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .models import Space, SpaceAddress, Amenity, Room
from .forms import NewSpaceForm, RoomFormSet, AmenityFormSet


def new_space(request):
    #RoomFormSetClass = modelformset_factory(Room, form=RoomFormSet, extra=1)

    if request.method == 'POST':
        form = NewSpaceForm(request.POST, request.FILES)
        room_formset = RoomFormSet(request.POST, prefix='rooms')
        amenity_formset = AmenityFormSet(request.POST, prefix='amenities')

        # Verificar validez de los formularios
        if form.is_valid() and room_formset.is_valid() and amenity_formset.is_valid():
            # Crear dirección
            address = SpaceAddress.objects.create(
                street=form.cleaned_data['street'],
                street_number=form.cleaned_data['street_number'],
                floor=form.cleaned_data['floor'],
                apartment=form.cleaned_data['apartment'],
                reference=form.cleaned_data['reference'],
                city=form.cleaned_data['city'],
                department=form.cleaned_data['department'],
                province=form.cleaned_data['province']
            )

            # Crear espacio
            space = form.save(commit=False)
            space.address = address
            space.owner = request.user
            space.save()

            # Guardar habitaciones relacionadas
            rooms = room_formset.save(commit=False)
            for room in rooms:
                room.space = space
                room.save()

            # Guardar las amenities relacionadas
            amenities = amenity_formset.save(commit=False)
            for amenity in amenities:
                amenity.space = space
                amenity.save()

            # Guardar imágenes
            files = request.FILES.getlist('files')
            for file in files:
                File.objects.create(space=space, file=file)

            return redirect('home_view')
        else:
            # Si hay errores, renderiza los formularios con errores
            return render(request, 'add_space.html', {
                'form': form,
                'room_formset': room_formset,
                'amenity_formset': amenity_formset,
            })
    else:
        form = NewSpaceForm()
        room_formset = RoomFormSet(prefix='rooms')
        amenity_formset = AmenityFormSet(prefix='amenities')

        return render(request, 'add_space.html', {
            'form': form,
            'room_formset': room_formset,
            'amenity_formset': amenity_formset,
        })

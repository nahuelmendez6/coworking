from sys import prefix

from django.core.files import File
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .models import Space, SpaceAddress, Amenity, Room
from .forms import NewSpaceForm, RoomFormSet


def new_space(request):
    if request.method == 'POST':
        form = NewSpaceForm(request.POST, request.FILES)
        room_formset = RoomFormSet(request.POST, prefix='rooms')

        if form.is_valid() and room_formset.is_valid():
            try:
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

                space = form.save(commit=False)
                space.address = address
                space.owner = request.user
                space.save()

                rooms = room_formset.save(commit=False)
                amenities = form.cleaned_data['amenities']
                #room_images = request.FILES.getList('roomImage')

                for room in rooms:
                    room.space = space
                    room.save()
                    for amenity in amenities:
                        room.amenities.add(amenity)


                return redirect('home_view')

            except Exception as e:
                print(f"Error al guardar los datos: {e}")

        else:
            print("Errores en el formulario principal:", form.errors)
            print("Errores en el conjunto de formularios:", room_formset.errors)

        return render(request, 'add_space.html', {
            'form': form,
            'room_formset': room_formset,
        })

    else:
        form = NewSpaceForm()
        room_formset = RoomFormSet(prefix='rooms')

        return render(request, 'add_space.html', {
            'form': form,
            'room_formset': room_formset,
        })

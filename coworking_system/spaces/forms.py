from django import forms

from .models import Space, SpaceAddress, Amenity, Room, Review, SpaceImage, WorkingHours, City, Department, Province

class NewSpaceForm(forms.ModelForm):

    # Campos adicionales del modelo SpaceAddress
    street = forms.CharField(max_length=100, label='Calle')
    street_number = forms.CharField(max_length=10, label='Número')
    floor = forms.CharField(max_length=10, label='Piso')
    apartment = forms.CharField(max_length=10, label='Departamento')
    reference = forms.CharField(widget=forms.Textarea, required=False, label="Referencia")

    # FK para ciudad, departamento y provincia
    city = forms.ModelChoiceField(queryset=City.objects.all(), label="Ciudad")
    department = forms.ModelChoiceField(queryset=Department.objects.all(), label="Localidad")
    province = forms.ModelChoiceField(queryset=Province.objects.all(), label="Provincia")

    # Campos adicionales para SpaceAmenities
    amenities_name = forms.CharField(max_length=100, label="Nombre")
    description = forms.Textarea()

    # Campos adicionales para Room
    room_name = forms.CharField(max_length=100, label="Nombre habitación")
    capacity = forms.IntegerField(label="Capacidad")
    price_per_hour = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio por hora")

    # Campo para cargar las imagenes
    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple':True}),
        required=False,
        label='Carga imágenes del espacio'
    )

    class Meta:
        model = Space
        fields = ['name', 'description', 'capacity', 'street', 'street_number',
                  'floor', 'apartment', 'reference', 'city', 'department', 'province', 'amenities_name', 'description',
                  'room_name', 'capacity', 'price_per_hour', 'images']
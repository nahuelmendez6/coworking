from django import forms
from django.forms import inlineformset_factory

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

    # Campo para seleccionar amenities
    amenities = forms.ModelMultipleChoiceField(
        queryset=Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Comodidades disponibles"
    )



    # Campo para cargar las imagenes
    images = forms.ImageField(
        widget=forms.FileInput(),
        required=False,
        label="Cargar imágenes del espacio"
    )

    class Meta:
        model = Space
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.basic_info = ['name', 'description', 'capacity']
        self.address = ['street', 'street_number', 'floor', 'apartment', 'reference', 'city', 'department', 'province']


# Formulario para Room
RoomFormSet = inlineformset_factory(
    Space, Room,
    fields=['room_name', 'capacity', 'price_per_hour', 'description'],
    extra=1,
    can_delete=True
)


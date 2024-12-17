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

    class Meta:
        model = Space
        fields = ['name', 'description', 'capacity', 'street', 'street_number',
                  'floor', 'apartment', 'reference', 'city', 'department', 'province']
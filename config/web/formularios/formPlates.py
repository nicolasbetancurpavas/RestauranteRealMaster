from django import forms


class FormPlates(forms.Form):

    PLATES = (
        (1, 'Entradas'),
        (2, 'Plato fuerte'),
        (1, 'postre')
    )

    name = forms.CharField(
        required=True,
        max_length=20,
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-inputs mb-2'})
    )

    description = forms.CharField(
        required=True,
        max_length=200,
        label='Description',
        widget=forms.Textarea(attrs={'class': 'form-inputs text-area mb-2'})
    )

    image = forms.CharField(
        required=True,
        label='Imagen',
        widget=forms.TextInput(attrs={'class': 'form-inputs mb-2'})
    )

    price = forms.CharField(
        required=True,
        max_length=20,
        label='Precio',
        widget=forms.NumberInput(attrs={'class': 'form-inputs mb-2'})
    )

    type = forms.ChoiceField(
        required=True,
        label='Tipo de plato',
        widget=forms.Select(attrs={'class': 'form-inputs mb-2'}),
        choices=PLATES
    )

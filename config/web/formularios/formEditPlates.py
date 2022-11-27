from django import forms


class FormEdit (forms.Form):

    PLATES = (
        (1, 'Entradas'),
        (2, 'Plato fuerte'),
        (1, 'postre')
    )

    name = forms.CharField(
        required=True,
        max_length=20,
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-input-edit mb-2'})
    )

    description = forms.CharField(
        required=True,
        max_length=200,
        label='Description',
        widget=forms.Textarea(
            attrs={'class': 'form-input-edit mb-2 text-area'})
    )

    price = forms.CharField(
        required=True,
        max_length=20,
        label='Precio',
        widget=forms.NumberInput(attrs={'class': 'form-input-edit mb-2'})
    )

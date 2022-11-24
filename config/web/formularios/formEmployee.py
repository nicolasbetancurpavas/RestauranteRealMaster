from django import forms


class FormEmployee (forms.Form):

    POSITION = (
        (1, 'Chef'),
        (2, 'Administrador'),
        (3, 'Mesero'),
        (4, 'Auxiliar'),
    )

    nombre = forms.CharField(
        required=True,
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'inputs-form-employee mb-1'})
    )

    apellido = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'inputs-form-employee mb-1'})
    )

    foto = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'inputs-form-employee mb-1'})
    )

    salario = forms.CharField(
        required=True,
        max_length=12,
        widget=forms.NumberInput(attrs={'class': 'inputs-form-employee mb-1'})
    )

    contacto = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class': 'inputs-form-employee mb-1'})
    )

    cargo = forms.ChoiceField(
        required=True,
        label='',
        widget=forms.Select(attrs={'class': 'inputs-form-employee mb-1'}),
        choices=POSITION
    )

from cProfile import label
from django import forms
from patients.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'first_name', 'last_name', 'date_of_birth', 'gender',
            'phone_1', 'phone_2', 'email'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: João'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Silva'}),
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'},
                format='%Y-%m-%d'  # <- formato que o input date espera
            ),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'phone_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(99) 99999-9999'}),
            'phone_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(99) 99999-9999'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
        }

        labels = {
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
            'date_of_birth': 'Data de Nascimento',
            'gender': 'Gênero',
            'phone_1': 'Telefone 1',
            'phone_2': 'Telefone 2',
            'email': 'E-mail',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.date_of_birth:
            self.fields['date_of_birth'].initial = self.instance.date_of_birth
        self.fields['date_of_birth'].input_formats = ['%Y-%m-%d']

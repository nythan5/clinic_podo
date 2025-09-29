from cProfile import label
from django import forms
from procedures.models import Procedure


class ProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = ['patient', 'name', 'procedure_date', 'notes']

        widgets = {
            'procedure_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do procedimento'}),
            'patient': forms.Select(attrs={'class': 'form-select'}),
        }

        labels = {
            'patient': 'Paciente',
            'name': 'Nome do Procedimento',
            'procedure_date': 'Data do Procedimento',
            'notes': 'Observações',
        }

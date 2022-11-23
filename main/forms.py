from django import forms
from main.models import Candidato

class DatePickerInput(forms.DateInput):
        input_type = 'date'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'


class CandidatoForm(forms.ModelForm):
    class Meta:
        model=Candidato
        fields= '__all__'   

        widgets = {
            'minicursos': forms.CheckboxSelectMultiple(),
            'sexo': forms.RadioSelect(),
            'data_nascimento': forms.TimeInput(attrs={'type': 'date'}),
        }
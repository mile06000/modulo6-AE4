from django import forms
from .models import Evento, Participante
from datetime import date

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'ubicacion']

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha <= date.today():
            raise forms.ValidationError("La fecha debe ser futura.")
        return fecha


class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = ['nombre', 'correo']

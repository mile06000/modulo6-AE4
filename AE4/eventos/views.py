from django.shortcuts import render, redirect
from .forms import EventoForm
from .models import Evento


# 👉 Vista para registrar un evento
def registrar_evento(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    
    return render(request, "eventos/evento_form.html", {"form": form})


# 👉 Vista para listar los eventos (AGREGA ESTA)
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, "eventos/lista_eventos.html", {"eventos": eventos})

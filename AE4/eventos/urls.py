from django.urls import path
from .views import registrar_evento, lista_eventos

urlpatterns = [
    path('registrar/', registrar_evento, name='registrar_evento'),
    path('lista/', lista_eventos, name='lista_eventos'),
]

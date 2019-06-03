from django.urls import path

from demo_leafletjs.views import mapa

urlpatterns = [
    path('mapa/', mapa, name='mapa'),
]

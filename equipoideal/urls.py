
from django.urls import path
from equipoideal import views

urlpatterns = [
#    path('jugar/', vw, name='templated'),

    path('juegoequipoideal/', views.JuegoEquipoIdeal, name='juegoequipoideal'),

    ]

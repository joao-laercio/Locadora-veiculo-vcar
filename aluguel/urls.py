from django.urls import path
from .views import index, listar_carros, realizar_aluguel, detalhar_carro, realizar_aluguel_carro, listar_alugueis

urlpatterns = [
    path('', index, name='index'),
    path('carros/', listar_carros, name='listar_carros'),
    path('alugueis/', listar_alugueis, name='listar_alugueis'),
    path('carros/<int:pk>', detalhar_carro, name='detalhar_carro'),
    path('carros/aluguel/<int:carro_pk>', realizar_aluguel_carro, name='realizar_aluguel_carro' ),
    path('aluguel/add', realizar_aluguel, name='realizar_aluguel'),
]

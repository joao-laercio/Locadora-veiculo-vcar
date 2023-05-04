from django.urls import path
from .views import index, listar_carros, realizar_aluguel, detalhar_carro, realizar_aluguel_carro, listar_alugueis,cadastrar_carro, atualizar_carro, deletar_carro

urlpatterns = [
    path('', index, name='index'),
    path('carros/', listar_carros, name='listar_carros'),
    path('alugueis/', listar_alugueis, name='listar_alugueis'),
    path('carros/<int:pk>', detalhar_carro, name='detalhar_carro'),
    path('carros/aluguel/<int:carro_pk>', realizar_aluguel_carro, name='realizar_aluguel_carro' ),
    path('aluguel/add', realizar_aluguel, name='realizar_aluguel'),
]


# urlpatterns = [
#     path('carro/', listar_carros, name='listar_carros'),
#     path('carro/<int:pk>', detalhar_carro, name='detalhar_carro'),
#     path('carro/cadastrar.html', cadastrar_carro, name='cadastrar_carro'),
#     path('carro/atualizar/<int:pk>', atualizar_carro, name='atualizar_carro'),
#     path('carro/deletar/<int:pk>', deletar_carro, name='deletar_carro'),

    
# ]
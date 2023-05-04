from django.shortcuts import render, redirect
from .models import Carro, Aluguel, Cliente
from django.contrib.auth.decorators import login_required, permission_required
from .forms import AluguelForm, CarroForm, MyUserCreationForm





# Create your views here.

def index(request):
    carros = Carro.objects.all()[:5]
    return render(request, 'index.html', {"carros":carros})

def listar_carros(request):
    carros = Carro.objects.all()
    return render(request, 'carro/listar.html', {"carros":carros})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/listar.html', {"clientes":clientes})

def detalhar_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    return render(request, 'cliente/detalhar.html', {"cliente":cliente})
    
def listar_alugueis(request):
    alugueis = Aluguel.objects.all()
    return render(request, 'aluguel/listar.html', {"alugueis":alugueis})

def detalhar_carro(request, pk):
    carro = Carro.objects.get(pk=pk)
    return render(request, 'Carro/detalhar.html', {"carro":carro})

@login_required
@permission_required('carros.add_carro')
def cadastrar_carro(request):
    if request.method == "POST":
        form = CarroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = CarroForm()
            return render(request, "carro/cadastrar.html", {'form': form})
    else:
        form = CarroForm()
        return render(request, "carro/cadastrar.html", {'form': form})
        

@login_required
@permission_required('carros.change_carro')
def atualizar_carro(request, pk):
    autor = Carro.objects.get(pk=pk)
    form = CarroForm(instance=Carro)
    
    if request.method == "POST":
        form = CarroForm(request.POST, request.FILES, instance=Carro)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, "autor/atualizar.html", {'form': form})
    else:
        return render(request, "autor/atualizar.html", {'form': form})

@login_required
@permission_required('carros.delete_carro')
def deletar_carro(request, pk):
    carro = Carro.objects.get(pk=pk)

    if carro:
        carro.delete()
        return redirect("carros/carro")
    else:
        return render(request, "carro/listar.html", {'msg': "Carro não encontrado"})

def registration(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = MyUserCreationForm()
            return render(request, "registration/registration.html", {'form': form})
    else:
        form = MyUserCreationForm()
        return render(request, "registration/registration.html", {'form': form})

def realizar_aluguel(request, pk):
    aluguel = Aluguel.objects.get(pk=pk)
    form = AluguelForm(instance=aluguel)
    
    if request.method == "POST":
        form = AluguelForm(request.POST, request.FILES, instance=aluguel)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, "aluguel/cadastrar.html", {'form': form})
    else:
        return render(request, "aluguel/cadastrar.html", {'form': form})

# def realizar_aluguel(request):
#     if request.method == "POST":
#         form = AluguelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             form = AluguelForm()
#             return render(request, "aluguel/cadastrar.html", {'form': form})
#     else:
#         form = AluguelForm()
#         return render(request, "aluguel/cadastrar.html", {'form': form})

def realizar_aluguel_carro(request, carro_pk):
    carro = Carro.objects.get(pk=carro_pk)
    aluguel = Aluguel()
    aluguel.carro = carro
    
    form = AluguelForm(instance=aluguel)
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AluguelForm(instance=aluguel)
            return render(request, "aluguel/cadastrar.html", {'form': form})
    else:
        form = AluguelForm(instance=aluguel)
        return render(request, "aluguel/cadastrar.html", {'form': form})
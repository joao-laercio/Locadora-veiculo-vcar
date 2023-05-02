from django.contrib import admin
from .models import Cliente, Carro, Aluguel

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Aluguel)
admin.site.register(Carro)

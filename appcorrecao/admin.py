from django.contrib import admin
from .models import Pessoa, Funcionario, Departamento, Processo, Documento, Portaria, Prazo, Envio, Tramitacoes

admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Departamento)
admin.site.register(Processo)
admin.site.register(Documento)
admin.site.register(Portaria)
admin.site.register(Prazo)
admin.site.register(Envio)
admin.site.register(Tramitacoes)
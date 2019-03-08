from django.contrib import admin
# testar se deu certo o banco adicionando na /admin
from .models import Categoria
from .models import Transacao

#Deixar disponivel no site /admin
admin.site.register(Categoria)
admin.site.register(Transacao)

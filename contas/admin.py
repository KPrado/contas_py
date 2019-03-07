from django.contrib import admin
# testar se deu certo o banco
from .models import Categoria

#Deixar disponivel no site /admin
admin.site.register(Categoria)

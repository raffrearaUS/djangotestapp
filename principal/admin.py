from django.contrib import admin
from .models import Diario, Usuario, Noticia, Autor

admin.site.register(Diario)
admin.site.register(Usuario)
admin.site.register(Noticia)
admin.site.register(Autor)

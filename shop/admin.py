from django.contrib import admin
from .models import Remera

# Register your models here.
#admin.site.register(Remera)

#Definimos la admin class
class RemeraAdmin(admin.ModelAdmin):
    list_display = ('marca' , 'talle', 'color', 'lisa', 'genero')
    list_filter = ('genero', 'talle')


#Registramos la admin class con el modelo asociado
admin.site.register(Remera, RemeraAdmin)
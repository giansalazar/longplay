from django.contrib import admin
from .models import *

# Register your models here.

class PersonasAdmin(admin.ModelAdmin):
    list_display = ('nombre','apep', 'apem',)
    search_fields = ('nombre','apep', 'apem',)

class ContinentesAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class PaisesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id_continente_id',)
    search_fields = ('nombre', 'id_continente_id',)

class GenerosAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class ArtistasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id_pais_id',)
    search_fields = ('nombre', 'id_pais_id',)

class AlbumesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id_artista_id', 'id_genero_id', 'anio_publicacion', 'num_canciones')
    search_fields = ('nombre', 'id_artista_id', 'id_genero_id', 'anio_publicacion', 'num_canciones')

class CancionesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id_album_id', 'duracion',)
    search_fields = ('nombre', 'id_album_id', 'duracion',)

class DiscosAdmin(admin.ModelAdmin):
    list_display = ('id_album_id', 'id_pais_fabricacion_id', 'edicion', 'condicion')
    search_fields = ('id_album_id', 'id_pais_fabricacion_id', 'edicion', 'condicion')


class PublicacionesAdmin(admin.ModelAdmin):
    list_display = ('id_disco_id', 'fecha_pub', 'precio', 'descripcion', 'id_usuario_id')
    search_fields = ('id_disco_id', 'fecha_pub', 'precio', 'descripcion', 'id_usuario_id')


admin.site.register(Personas, PersonasAdmin)
admin.site.register(Continentes, ContinentesAdmin)
admin.site.register(Paises, PaisesAdmin)
admin.site.register(Generos, GenerosAdmin)
admin.site.register(Artistas, ArtistasAdmin)
admin.site.register(Albumes, AlbumesAdmin)
admin.site.register(Canciones, CancionesAdmin)
admin.site.register(Discos, DiscosAdmin)
admin.site.register(Publicaciones, PublicacionesAdmin)
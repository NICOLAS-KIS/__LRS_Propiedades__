from django.contrib import admin
from .models import Propiedad, PropiedadImagen, Photo
from . import views as v

class PropiedadImagenInline(admin.TabularInline):
    model = PropiedadImagen

class PropiedadAdmin(admin.ModelAdmin):
    list_display = ["titulo", "localidad", "tipo"]
   # inlines = [PropiedadImagenInline,  ]

    list_filter = ('titulo',)

    def save_model(self, request, obj, form, change):
        id = obj.id
        print(id)
        v.Upload(request, id)
        super().save_model(request, obj, form, change)

    class Meta:
        model = Propiedad

    def __str__(self):
        return "prueba"

admin.site.register(Propiedad, PropiedadAdmin)

class PhotoAdmin(admin.ModelAdmin):

    class Meta:
        model = Photo

admin.site.register(Photo, PhotoAdmin)















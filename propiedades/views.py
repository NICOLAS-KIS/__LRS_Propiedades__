from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Propiedad, PropiedadImagen, Photo


def propiedades_list(request):
    queryset = Propiedad.objects.filter(id=2)
    #property = Property.objects.get(pk=1)
    newqueryset = Photo.objects.all()
    print( newqueryset )
    context = {
        "imagenes" : newqueryset,
        "propiedades" : queryset,
    }
    template = 'newslide.html'
    return render(request, template, context)

def propiedades_detalle(request, id = None):
    queryset = Propiedad.objects.filter(id=id)
    #property = Property.objects.get(pk=1)
    newqueryset = Photo.objects.all()
    print( newqueryset )
    context = {
        "imagenes" : newqueryset,
        "propiedades" : queryset,
    }
    template = 'newslide.html'
    return render(request, template, context)


def filter_by_operacion(request, id=None):
    #instance = get_object_or_404(Propiedad, id = id)
    queryset = Propiedad.objects.filter(operacion__icontains="Venta")
    context = {
        "title" : queryset.titulo,
        "propiedades" : queryset,
    }
    template = 'home.html'
    return render(request, template, context)
                  #"pruebas/pruebas.html", context)

def Form(request):
    return render(request,"index/form.html",{})

def Upload(request, id):
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f):
            Photo.objects.create(image = f, propiedad_id = id)
            # Guarda las imagenes donde pida
            #with open('static/media/' + id + '__file' + str(count) + '.jpg', 'wb+') as destination:
            #    for chunk in f.chunks():
            #        destination.write(chunk)
        process(x)
    return HttpResponse("File(s) uploaded!")


"""def imagen_list(request):
    property = PropiedadImagen.objects.all #get(pk=1)
    queryset = property.images.all()
    context = {
        "imagenes" : queryset,
    }
    template = 'propiedades.html'
    return render(request, template, context)"""


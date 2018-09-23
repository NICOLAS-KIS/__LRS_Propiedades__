from django.shortcuts import render
from propiedades.models import Propiedad

def home(request):

    template = 'home.html'
    queryset_list = Propiedad.objects.all()

    query = request.GET.get("featured")
    print(" none value ? %s ", query)

    if query in ['A', 'V']:
        print("..........................................")
        queryset_list = queryset_list.filter(
            operacion__exact=query
        ).distinct()
    context = {
        "propiedades" : queryset_list,
    }

    return render(request, template, context)

def about(request):

    context = locals()
    return render(request, template_name, context_dict)


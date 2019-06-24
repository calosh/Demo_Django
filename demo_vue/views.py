from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.template import Context, Template
from django.db.models import Q
from django.core.paginator import EmptyPage

from .models import Producto, Categoria


def index_vue(request):
    categorias = Categoria.objects.all()
    print(categorias)
    print(categorias.get_ancestors())
    return render(request, "vue/index.html", {"categorias":categorias})

def get_products(request):
    page = request.GET.get("page") if request.GET.get("page") else 1
    categoria = request.GET.get("categoria") if request.GET.get("categoria") else None
    subCategoria = request.GET.get("subCategoria") if request.GET.get("subCategoria") else None
    busqueda = request.GET.get("busqueda") if request.GET.get("busqueda") else None
    
    if categoria:
        queryset = Producto.objects.filter(categoria__parent=categoria)
    elif subCategoria:
        queryset = Producto.objects.filter(categoria=subCategoria)
    elif busqueda:
        queryset = Producto.objects.filter(Q(nombre__icontains = busqueda) | Q(descripcion__icontains = busqueda))
    else:
        queryset = Producto.objects.all()

    for prod in queryset:
        c = Context({'image': prod})
        t = Template('{% load thumbnail %}{% thumbnail image.imagen "100x100" as img %}<img src="{{img.url}}" height="{{img.height}}" width="{{img.width}}">{% endthumbnail %}')
        prod.imagen_src = t.render(c)
    
    try:
        paginador = Paginator(queryset, 3)
        productos = paginador.page(page)
    except EmptyPage:
        return JsonResponse({})
    return JsonResponse({
            'has_next':productos.has_next(),
            'has_previous':productos.has_previous(),
            'num_pages':paginador.num_pages,
            'count':paginador.count,
            'results': [
                {
                    'id': producto.pk,
                    'nombre': producto.nombre,
                    'descripcion': producto.descripcion,
                    'imagen_src':producto.imagen_src,
                }
                for producto in productos
            ],
        }) 
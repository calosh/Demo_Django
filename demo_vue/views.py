from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.template import Context, Template

from .models import Producto, Categoria


def index_vue(request):
    categorias = Categoria.objects.all()
    print(categorias)
    print(categorias.get_ancestors())
    return render(request, "vue/index.html", {"categorias":categorias})

def get_products(request):
    if request.GET.get("page"):
        page = request.GET.get("page")
    else:
        page = 1

    categoria = None
    subCategoria = None
    if request.GET.get("categoria"):
        categoria = request.GET.get("categoria")
    if request.GET.get("subCategoria"):
        subCategoria = request.GET.get("subCategoria")
    
    
    if categoria:
        queryset = Producto.objects.filter(categoria__parent=categoria)
    elif subCategoria:
        queryset = Producto.objects.filter(categoria=subCategoria)
    else:
        queryset = Producto.objects.all()

    for prod in queryset:
        c = Context({'image': prod})
        t = Template('{% load thumbnail %}{% thumbnail image.imagen "100x100" as img %}<img src="{{img.url}}" height="{{img.height}}" width="{{img.width}}">{% endthumbnail %}')
        prod.imagen_src = t.render(c)
    
    paginador = Paginator(queryset, 3)
    productos = paginador.page(page)
    return JsonResponse({
            'count': len(productos),
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
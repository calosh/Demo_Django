from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse, HttpResponse


def suma(request):

    total = 0
    valor = 0

    if request.is_ajax():
        if request.GET:
            valor = int(request.GET['numero'])
            
        if request.POST:
            valor = int(request.POST['numero'])
        
        total = int(valor) * 100
        response = JsonResponse({'total':total})

        return HttpResponse(response.content)
    return render(request, 'index.html', {"total":total, "valor": valor})

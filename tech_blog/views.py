
from django.shortcuts import render
from django.template.response import TemplateResponse
# Create your views here.

#making the search bar work
def Search(request):

    search = request.POST.get('search_nav')
    prueba = 'prueba'
    return TemplateResponse(request, 'templates/home/home_page.html', {
        'search_bar': search,
        "prueba1": prueba
    })




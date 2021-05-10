from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Allcources
from django.template import loader

def Cources(request):
    ac = Allcources.objects.all()
    template=loader.get_template('TechnicalCources/Cources.html')
    context={
        'ac':ac,
    }
    return HttpResponse(template.render(context, request))

def detail(request, couse_id):
    try:
        course=Allcources.objects.get(pk=couse_id)
    except Allcources.DoesNotExist:
        raise Http404("Cource Not Available")

    return render(request, 'TechnicalCources/detail.html', {'course':course})

from django.shortcuts import render
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
import json
from .models import *
from django.http import JsonResponse


def HomeCtrl(request):
    sp = SpainPortugal.objects.all()
    np = NubePalabras.objects.all()
    f = FollowData.objects.all()
    hc = HashCount.objects.all()
    return render(request, 'home.html', {'sp': sp, 'np': np, 'f': f, 'hc': hc, 'home': True})


def SpainPortugalCtrl(request):
    data = list(SpainPortugal.objects.values())
    return JsonResponse(data, safe=False)


def NubeCtrl(request):
    return render(request, 'nube_palabras.html')


def NubeDataCtrl(request):
    data = list(NubePalabras.objects.values())
    return JsonResponse(data, safe=False)


def PaginaFolloIngErCtrl(request):
    return render(request, 'follow_ing_ers.html')


def PaginaFolloIngErDataCtrl(request):
    data = list(FollowData.objects.values())
    return JsonResponse(data, safe=False)

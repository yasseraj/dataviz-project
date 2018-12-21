from django.shortcuts import render
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
import json
from .models import *
from django.http import JsonResponse


def HomeCtrl(request):
    # sp = SpainPortugal.objects.all()
    np = NubePalabras.objects.all()
    f = FollowData.objects.all()
    hc = HashCount.objects.all()
    th = TimeTweets.objects.all()
    dt = DayTweets.objects.all()
    #return render(request, 'home.html', {'sp': sp, 'np': np, 'f': f, 'hc': hc, 'th': th, 'home': True})
    return render(request, 'home.html', {'np': np, 'f': f, 'hc': hc, 'th': th, 'dt': dt, 'home': True})


def SpainPortugalCtrl(request):
    data = list(SpainPortugal.objects.values())
    return JsonResponse(data, safe=False)


def NubeCtrl(request):
    return render(request, 'nube_palabras.html')


def NubeDataCtrl(request):
    data = list(NubePalabras.objects.values())
    return JsonResponse(data, safe=False)


def PaginaFolloIngErCtrl(request):
    return render(request, 'barras_followers.html')


def PaginaFolloIngErDataCtrl(request):
    data = list(FollowData.objects.values())
    return JsonResponse(data, safe=False)


def PaginaFolloIngErDataCtrl1(request):
    data = list(FollowData.objects.values())
    data = sorted(data, key=lambda k: -k['following'])
    return JsonResponse(data, safe=False)


def PaginaFolloIngErDataCtrl2(request):
    data = list(FollowData.objects.values())
    data = sorted(data, key=lambda k: -k['ratio'])
    return JsonResponse(data, safe=False)


def BurbujaCtrl(request):
    return render(request, 'burbujas.html')


def BurbujaDataCtrl(request):
    data = list(HashCount.objects.values())
    return JsonResponse(data, safe=False)


def LineasCtrl(request):
    return render(request, 'lineas.html')


def LineasDataCtrl(request):
    data_qs = TimeTweets.objects.all()
    data = []
    for d in data_qs:
        data.append(d.repeats)
    return JsonResponse({'tweets': data}, safe=False)


def LineasDataCtrl1(request):
    data_qs = DayTweets.objects.all()
    data = []
    for d in data_qs:
        data.append(d.num)
    return JsonResponse({'tweets': data}, safe=False)
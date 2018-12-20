from django.shortcuts import render
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
import json
from .models import *
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def graph(request):
    return render(request, 'graph/graph.html')


def SpainPortugalCtrl(request):
    data = list(SpainPortugal.objects.values())
    return JsonResponse(data, safe=False)


def PaginaNube(request):
    return render(request, 'nube.html')


def NubePalabrasCtrl(request):
    data = list(NubePalabras.objects.values())
    return JsonResponse(data, safe=False)


def PaginaFolloIngErCtrl(request):
    return render(request, 'follow_ing_ers.html')


def PaginaFolloIngErDataCtrl(request):
    data = list(FollowData.objects.values())
    return JsonResponse(data, safe=False)

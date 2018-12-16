from django.shortcuts import render
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
import json
from .models import SpainPortugal
from django.http import JsonResponse

def graph(request):
    return render(request, 'graph/graph.html')


def SpainPortugalCtrl(request):
    data = list(SpainPortugal.objects.values())
    return JsonResponse(data, safe=False)
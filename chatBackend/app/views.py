from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index(request):
    return HttpResponse("All goes well")

def json(request):
    return JsonResponse({"key":"value"})

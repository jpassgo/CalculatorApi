import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sum():
     return HttpResponse(
        'sum',
        content_type="application/json"
    )

@csrf_exempt
def difference():
    return HttpResponse(
        'sum',
        content_type="application/json"
    )

@csrf_exempt
def multiply():
    return HttpResponse(
        'sum',
        content_type="application/json"
    )

@csrf_exempt
def divide():
    return HttpResponse(
        'sum',
        content_type="application/json"
    )
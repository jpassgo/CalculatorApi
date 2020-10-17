import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def sum(request):
    request_body = json.loads(request.body)
    sum_of_two_operands = sum_operands(request_body['first_operand'], request_body['second_operand'])
    return HttpResponse(
        json.dumps({'sum': sum_of_two_operands}),
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

def sum_operands(first_operand, second_operand):
    return float(first_operand) + float(second_operand)
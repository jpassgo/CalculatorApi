import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def sum(request):
    request_body = json.loads(request.body)
    sum_of_two_operands = sum_operands(
        request_body['first_operand'],
        request_body['second_operand'])
    return HttpResponse(
        json.dumps({'sum': sum_of_two_operands}),
        content_type="application/json"
    )


@csrf_exempt
def difference(request):
    request_body = json.loads(request.body)
    difference_of_two_operands = difference_of_operands(
        request_body['first_operand'], request_body['second_operand'])
    return HttpResponse(
        json.dumps({'difference': difference_of_two_operands}),
        content_type="application/json"
    )


@csrf_exempt
def multiply(request):
    request_body = json.loads(request.body)
    product_of_two_operands = product_of_operands(request_body['first_operand'], request_body['second_operand'])
    return HttpResponse(
        json.dumps({'product': product_of_two_operands}),
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


def difference_of_operands(first_operand, second_operand):
    return float(first_operand) - float(second_operand)

def product_of_operands(first_operand, second_operand):
    return float(first_operand) * float(second_operand)
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def sum(request):
    request_body = json.loads(request.body)
    sum = sum_operands(
        request_body['first_operand'],
        request_body['second_operand'])
    return HttpResponse(
        json.dumps({'sum': sum}),
        content_type="application/json"
    )


@csrf_exempt
def difference(request):
    request_body = json.loads(request.body)
    difference = difference_of_operands(
        request_body['first_operand'], request_body['second_operand'])
    return HttpResponse(
        json.dumps({'difference': difference}),
        content_type="application/json"
    )


@csrf_exempt
def multiply(request):
    request_body = json.loads(request.body)
    product = product_of_operands(
        request_body['first_operand'],
        request_body['second_operand'])
    return HttpResponse(
        json.dumps({'product': product}),
        content_type="application/json"
    )


@csrf_exempt
def divide(request):
    request_body = json.loads(request.body)
    quotient = quotient_of_operands(
        request_body['first_operand'],
        request_body['second_operand'])
    return HttpResponse(
        json.dumps({'qoutient': quotient}),
        content_type="application/json"
    )


def sum_operands(first_operand, second_operand):
    return float(first_operand) + float(second_operand)


def difference_of_operands(first_operand, second_operand):
    return float(first_operand) - float(second_operand)


def product_of_operands(first_operand, second_operand):
    return float(first_operand) * float(second_operand)


def quotient_of_operands(first_operand, second_operand):
    return float(first_operand) / float(second_operand)

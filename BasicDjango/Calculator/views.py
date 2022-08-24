from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', { 'name': 'Vishal Chaurasiya' })


def add(request):
    res = int(request.GET['num1']) + int(request.GET['num2'])

    return render(request, 'result.html', { 'result': res })

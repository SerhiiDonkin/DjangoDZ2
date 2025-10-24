from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def app1(request: HttpRequest) -> HttpResponse:
    return render(request, 'app1/index1.html', {
        'dz1': 'Привіт, це 1 ДЗ',
    })


def home(request):
    return HttpResponse("Home")


def book(request, title):
    return HttpResponse(f"Заголовок книги: {title.capitalize()}")


def lesson_2(request):
    return HttpResponse("lesson_2")

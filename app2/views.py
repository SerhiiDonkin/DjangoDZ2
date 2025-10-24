from django.http import HttpResponse


def index(request):
    return HttpResponse("Ви на сторінці index.")


def app2(request):
    return HttpResponse("Ви на сторінці 2 ДЗ.")


def bio(request, name):
    return HttpResponse(f"Ім'я користувача: {name.capitalize()}")

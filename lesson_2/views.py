from django.http import HttpResponse


def lesson_2(request):
    return HttpResponse("Це щоб не було помилок у ДЗ. \n\nЄ такі сторінки як /app1 /app2 та /weather_app")
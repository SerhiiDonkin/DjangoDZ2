import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

WEATHER_TOKEN = settings.OPENWEATHER_APPID


def weather_app(request):
    city = request.GET.get('city')

    weather_api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}&units=metric&lang=uk"

    try:
        response = requests.get(weather_api, timeout=5)
        print(response.json())
        data = response.json()

        if data.get('cod') == '404':
            return HttpResponse(f'<script>alert("Населеного пункту {city} не існує!");</script>')

        if response.status_code != 200:
            return HttpResponse(f"Помилка з'єднання з погодним сервісом або проблема API ключем.")

        weather_info = {
            'country': data['sys']['country'],
            'city': data['name'],
            'coords': f"Довгота: {data['coord']['lon']}, Широта: {data['coord']['lat']}",
            'weather_main': data['weather'][0]['main'],
            'weather_description': data['weather'][0]['description'].capitalize(),
            'temp_celsius': f"{data["main"]["temp"]}°C",
        }

        return render(request, 'weather_app/index1.html', {'weather': weather_info})


    except requests.exceptions.RequestException as e:
        error_context = {'error_message': f'Сталася помилка мережі: {e}'}
        return render(request, 'weather_app/index1.html', error_context)

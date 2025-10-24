"""
Завдання 2

Складіть файл urls.py, який:

- направляє URL з 'index/' у метод views.index і
    задає ім'я для цього URL як 'index-view'.

- направляє URL з 'bio/{ім'я користувача}/' у метод views.bio
разом з ім'ям користувача як аргумент username та задає ім'я для цього URL як 'bio'.

 - передає запити, що починаються з 'lesson_1/'
    в модуль 'lesson_1.urls' разом із залишком URL.

"""

from django.urls import include, path

from . import views

urlpatterns = [
    # path('index/', views.index, name='index-view'),
    # path('bio/<str:name>/', views.bio, name='bio'),
    # path('lesson_1/', include('lesson_1')),
    path('', views.app2, name='app2'),

]

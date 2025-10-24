"""Складіть файл urls.py, який:
 - направляє URL з home/' у метод views.home і
 задає ім'я для цього URL як 'home-view';

- направляє URL з 'book/{назва глави}/' у метод views.
Book разом з назвою розділу як аргумент title та задає
ім'я для цього URL як 'book';

- передає запити, що починаються з 'lesson_2/' до
модуля 'lesson_2.urls' разом із залишком URL.

"""

from django.urls import include, path

from . import views

urlpatterns = [
    path('home/', views.home, name='home-view'),
    path('book/<str:title>/', views.book, name='book'),
    path('lesson_2/', include('lesson_2.urls')),
    path('', views.app1, name='app1'),

]

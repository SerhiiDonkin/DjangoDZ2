from django.urls import path

from . import views

urlpatterns = [
    path('', views.lesson_2, name='lesson_2'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('hello-world', views.hello_world),
    path('current-time', views.current_time)
]

urlpatterns = [
    path('licznik', views.licznik_view, name='licznik'),
]
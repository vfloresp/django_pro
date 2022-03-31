from django.contrib import admin
from django.urls import path


def DesdeAppsDep(self):
    print("==========DEPARTAMENTO============")


urlpatterns = [
    path("departamento/", DesdeAppsDep),
]

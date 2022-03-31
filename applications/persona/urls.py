from django.contrib import admin
from django.urls import path


def desde_app_persona(self):
    print("==========PERSONA============")


urlpatterns = [
    path("persona/", desde_app_persona),
]

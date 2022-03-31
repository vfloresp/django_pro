from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Included urls from dep app
    re_path("", include("applications.departamento.urls")),
    re_path("", include("applications.persona.urls")),
    re_path("", include("applications.home.urls")),
]

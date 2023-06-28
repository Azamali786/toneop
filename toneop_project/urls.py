from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("mainapp/", include("mainapp.urls", namespace="mainapp")),
]

api_urls = [path("api/", include("api.urls"))]

urlpatterns += api_urls

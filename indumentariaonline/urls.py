from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("shop/", include("shop.urls")),
    path('admin/', admin.site.urls)
]   
from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="chile"),
    path('plot/', views.plot),
    path('regiones/', views.regiones, name="regiones"),
    path('regions/', views.regions),
]

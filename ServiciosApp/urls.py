from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicios, name="Servicios"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria")
]

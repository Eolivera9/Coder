from django.urls import path
from AppCoder import views

urlpatterns = [

    path('inicio', views.inicio, name="Inicio"),
    path('jugadores', views.jugadores, name="Jugadores"),
    path('equipos', views.equipos, name="Equipos"),
    path('estadio', views.estadio, name="Estadio"),
    path('estadioFormulario', views.estadioFormulario),
    path('equipoFormulario', views.equipoFormulario),
    path('jugadorFormulario', views.jugadorFormulario),
    path('busquedaEquipo', views.busquedaEquipo),
    path('buscar/', views.buscar),

]
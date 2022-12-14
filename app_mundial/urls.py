from django.urls import path
from app_mundial import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('about',views.about, name="about"),
    # URLs de Jugadores
    path('jugadores/', views.jugadores, name="jugadores"),
    path('crear-jugadores/', views.jugadores_formulario, name="crear_jugadores"),
    path('busqueda-jugadores-form/', views.busqueda_jugadores, name="busqueda_jugadores_form"),
    path('busqueda-jugadores/', views.buscar_jugadores, name="busqueda_jugadores"),
    path('editar-jugadores/<int:id>/', views.editar_jugadores, name="editar_jugadores"),
    path('eliminar-jugadores/<int:id>/', views.eliminar_jugadores, name="eliminar_jugadores"),
    # URLs de Estadios
    path('estadios/', views.estadios, name="estadios"),
    path('crear-estadios/', views.estadios_formulario, name="estadios_formulario"),
    path('busqueda-estadios-form/', views.busqueda_estadios, name="busqueda_estadios_form"),
    path('busqueda-estadios/', views.buscar_estadios, name="busqueda_estadios"),
    path('editar-estadios/<int:id>/', views.editar_estadios, name="editar_estadios"),
    path('eliminar-estadios/<int:id>/', views.eliminar_estadios, name="eliminar_estadios"),
    # URLs de Selecciones
    path('seleciones/', views.selecciones, name="selecciones"),
    path('crear-selecciones/', views.selecciones_formulario, name="selecciones_formulario"),
    path('busqueda-selecciones-form/', views.busqueda_selecciones, name="busqueda_selecciones_form"),
    path('busqueda-selecciones/', views.buscar_selecciones, name="busqueda_selecciones"),
    path('editar-selecciones/<int:id>/', views.editar_selecciones, name="editar_selecciones"),
    path('eliminar-selecciones/<int:id>/', views.eliminar_selecciones, name="eliminar_selecciones"),
    # URLS Perfil
    path('editar-perfil/', views.ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', views.agregar_avatar, name="agregar_avatar"),
    # URLS Usuario y sesión
    path('login/', views.login_request, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.CustomLogoutView.as_view(), name = 'logout'),
  

]

from django.urls import path
from app_senauthenticator.controllers import programa, ficha, usuario, registro_facial, objeto, ingreso, tutor, oficina
# from app_senauthenticator.controllers.autenticacion_facial import AutenticacionFacial
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Oficina
    path('oficina/<int:pk>/', oficina.oficina_controlador, name="cont_oficina"),
    path('oficina/', oficina.oficina_controlador, name="cont_oficina"),
    # Programa
    path('programa/', programa.programa_controlador, name="cont_programa"),
    path('programa/<int:pk>/', programa.programa_controlador, name="cont_programa"),
    # Ficha
    path('ficha/', ficha.ficha_controlador, name="cont_ficha"),
    path('ficha/<int:pk>/', ficha.ficha_controlador, name="cont_ficha"),
    # Usuario
    path('usuario/', usuario.usuario_controlador, name="cont_usuario"),
    path('usuario/<int:pk>/', usuario.usuario_controlador, name="cont_usuario_detail"), 
    path('inicioSesion/', usuario.inicio_sesion, name="inicio_sesion"),
    path('validarToken/', usuario.validarToken, name='protected_view'),
    # Registro Facial
    path('registroFacial/', registro_facial.registro_facial_controlador),
    path('registroFacial/<int:pk>/', registro_facial.registro_facial_controlador),
    # Objeto
    path('objeto/', objeto.objeto_controlador, name="cont_objeto"),
    path('objeto/<int:pk>/', objeto.objeto_controlador, name="cont_objeto"),
    # Tutor
    path('tutor/', tutor.tutor_controlador),
    path('tutor/<int:pk>/', tutor.tutor_controlador),
    # Ingreso
    path('ingreso/', ingreso.ingreso_controlador, name="cont_ingreso"),
    path('ingreso/<int:pk>/', ingreso.ingreso_controlador, name="cont_ingreso"),
]



if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

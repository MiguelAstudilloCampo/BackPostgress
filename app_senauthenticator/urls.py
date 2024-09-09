from django.urls import path
from app_senauthenticator.controllers import programa, ficha, usuario, registro_facial, objeto, ingreso, tutor, oficina
# from app_senauthenticator.controllers.autenticacion_facial import AutenticacionFacial
from django.conf import settings
from django.conf.urls.static import static

# /////// importo rest_framework_simplejwt para el manejo de los tokens
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('oficina/<int:pk>/', oficina.oficina_controlador),
    path('oficina/', oficina.oficina_controlador),
    path('programa/', programa.programa_controlador),
    path('programa/<int:pk>/', programa.programa_controlador),
    path('ficha/', ficha.ficha_controlador),
    path('ficha/<int:pk>/', ficha.ficha_controlador),
    path('usuario/', usuario.usuario_controlador),
    path('usuario/<int:pk>/', usuario.usuario_controlador),
    path('inicioSesion/', usuario.inicio_sesion),
     path('validarToken/', usuario.validarToken, name='protected-view'),
    path('registroFacial/', registro_facial.registro_facial_controlador),
    path('registroFacial/<int:pk>/', registro_facial.registro_facial_controlador),
    path('objeto/', objeto.objeto_controlador),
    path('objeto/<int:pk>/', objeto.objeto_controlador),
    path('tutor/', tutor.tutor_controlador),
    path('tutor/<int:pk>/', tutor.tutor_controlador),
    path('ingreso/', ingreso.ingreso_controlador),
    path('ingreso/<int:pk>/', ingreso.ingreso_controlador),
    # path('perfil/', usuario.perfil),
    # path('autenticacionFacial/', AutenticacionFacial.as_view())
    
    
    # /////////////////////// token con jwt
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

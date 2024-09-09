# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from rest_framework.response import Response
# from rest_framework import status

# class CustomTokenObtainPairView(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         # Llamar a la implementación estándar
#         response = super().post(request, *args, **kwargs)
#         tokens = response.data  # Obtener los tokens generados
        
#         # Añadir los tokens a las cookies
#         response.set_cookie(
#             key='jwt-access',
#             value=tokens['access'],
#             httponly=True,
#             secure=False,  # Cambia a True en producción con HTTPS
#             samesite='Lax'
#         )
#         response.set_cookie(
#             key='jwt-refresh',
#             value=tokens['refresh'],
#             httponly=True,
#             secure=False,  # Cambia a True en producción con HTTPS
#             samesite='Lax'
#         )

#         # Elimina los tokens del cuerpo de la respuesta si no quieres exponerlos
#         del response.data['access']
#         del response.data['refresh']

#         return response

# class CustomTokenRefreshView(TokenRefreshView):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         tokens = response.data
        
#         # Actualizar la cookie con el nuevo access token
#         response.set_cookie(
#             key='jwt-access',
#             value=tokens['access'],
#             httponly=True,
#             secure=False,  # Cambia a True en producción con HTTPS
#             samesite='Lax'
#         )

#         # Elimina el token del cuerpo de la respuesta si no quieres exponerlo
#         del response.data['access']

#         return response

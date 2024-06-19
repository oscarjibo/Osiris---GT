"""
URL configuration for osiris_Dev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() ssfunction: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from osiris_dev.views import bienvenida, modulos, categoria_edad, plantilla1, plantilla_parametros, plantilla_cargador, plantilla_shortcut, plantillahija, plantillahija2
from aplicaciones.automatizacion.views import get_data_sensor, ia, chat, yolov5, actualizar_control_data,home, login, s1, s2, s3, get_data_sensor, inicio, support, enviar_mail


urlpatterns = [
    path("admin/", admin.site.urls),  
    path('', home, name='home'),
    path('salir', home, name='home'),   
    path('login', login, name='login'), 
    path("s1", s1, name='s1'),  
    path("s2", s2, name='s2'),
    path("inicio", inicio, name='inicio'), 
    path("control", s3, name='s3'),
    path("support", support, name='support'),
    path('enviar_mail', enviar_mail, name='enviar_mail'),
    path('yolov5', yolov5, name='yolov5'),
    path('chat', chat, name='chat'),
    path('ia', ia, name='ia'),
    
    path('get_data_sensor', get_data_sensor, name='get_data_sensor'),
    path('actualizar_control_data/', actualizar_control_data, name='actualizar_control_data')  # Agrega nombres a todas tus rutas
]

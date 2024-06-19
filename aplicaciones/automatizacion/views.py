from django.shortcuts import render, redirect
from django.contrib import messages
from .models import data, SensorData, ControlData, Support
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.http import HttpResponse
from datetime import datetime
import json 

def actualizar_control_data(request):
    if request.method == 'POST':
        estado_bomba1 = request.POST.get('estadoBomba1', '0')  # Obtiene el estado de la bomba1
        estado_bomba2 = request.POST.get('estadoBomba2', '0')  # Obtiene el estado de la bomba1
        print("ESTADO BOMBA 1: ", estado_bomba1)
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_insert = {"bomba1_state": estado_bomba1,
                       "bombas2_state": estado_bomba2,}
        # Aquí insertas una nueva fila en tu tabla ControlData
        control_data_insert = ControlData.objects.create(
            cliente= 'Juan Ochoa',  # Aquí debes poner el valor que corresponda
            fecha= f'{fecha}',  # Aquí se inserta la fecha y hora actual
            control_data= f'{data_insert}' # Aquí se inserta el objeto JSON
        )
        messages.success(request, 'Control actualizado correctamente')  # Aquí creas el mensaje
        return JsonResponse({'status': 'success'})
    
def home(request):
    users = data.objects.all()
    return render(request, "home.html", {"users": users})

def enviar_mail(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cliente = request.POST.get('cliente')
        problema = request.POST.get('problema')

        fecha = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Aquí insertas una nueva fila en tu tabla ControlData
        control_support_insert = Support.objects.create(
            estado=(nombre),
            cliente=(cliente),
            support_information=str(problema),
            fecha=fecha,
        )

        messages= 'Datos insertados       correctamente pulse para regresar    :'  # Aquí creas el mensaje
        return render(request, "support.html", {'messages': messages})
    else:
       return render(request, "support.html", {'messages': messages})

def get_data_sensor(request):
    if request.method == 'POST':
        print("POST request received")
        db_informations = SensorData.objects.values('DB_information')
        print("DB_information: ", db_informations)
        db_informations = [{"Luz_ultravioleta" : "20", "Presion_barometrica" : "30", "Luminosidad" : "40", "Lluvia" : "NO", "temperatura_aire" : "60", "Humedad_aire" : "70"}]
        print("DB_information: ", db_informations)
        return render(request, 's2.html', {"data": list(db_informations)})

def login(request):
    print("Función login_validate llamada")
    if request.method == 'POST':
        print("Método POST detectado")
        user_id = request.POST.get('user_id').strip()  # Elimina espacios en blanco
        password = request.POST.get('clave').strip()  # Elimina espacios en blanco
        print(f"user_id recibido: {user_id}, password recibida: {password}")
        try:
            print("=============")
            user = data.objects.get(id=user_id)
            # Convierte la clave a str antes de comparar, si es necesario
            if str(user.clave) == password:
                print("La contraseña es correcta, redirigiendo...")
                return render(request, "grid.html")
            else:
                print("La contraseña no coincide, mostrando mensaje de error")
                messages.error(request, 'Contraseña incorrecta')
        except data.DoesNotExist:
            print("El usuario no existe, mostrando mensaje de error")
            messages.error(request, 'El usuario no existe')
    
    print("Re-renderizando el formulario con la lista de usuarios")
    users = data.objects.all()
    return render(request, "home.html", {'users': users})


def s1(request):
    return render(request, "s1.html")

def s2(request):
    return render(request, "s2.html")

def s3(request):
    return render(request, "s3.html")

def inicio(request):
    return render(request, "grid.html")

def support(request):
    return render(request, "support.html")

def yolov5(request):
    return render(request, "yolov5.html")
def ia(request):
    return render(request, "ia.html")
def detector(request):
    return render(request, "detector.html")


#import google.generativeai as genai
#
## Create your views here.
## add here to your generated API key
#genai.configure(api_key="AIzaSyDDURhIdmkTmkxvPKTnya0kg63hGStcSkk")
#from django.views.decorators.csrf import csrf_exempt


def chat(request):
    pass
    """
    if request.method == 'POST':
        user_text = request.POST.get('user_text')
        if not user_text:
            user_text = "Hola, quiero que seas mi asistente de cultivo en el agro, por ahora saludame con algo decente y corto mi nombre es Juan Ochoa"
        model =genai.GenerativeModel("gemini-pro")
        print("USER TEXT: ", user_text)
        chat = model.start_chat()
        response = chat.send_message(user_text)
        response_data = {
            "text": response.text,
        }
        return render(request, 'chat.html', response_data)
    else:
        return render(request, 'chat.html')"""

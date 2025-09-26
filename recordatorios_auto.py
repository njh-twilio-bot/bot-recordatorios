
# =========================
# Código antiguo
# =========================
import os
from twilio.rest import Client
# print("Este era el código anterior")
# Aquí seguía tu lógica de recordatorios...

import datetime
print(f"🚀 Bot iniciado en Render a las {datetime.datetime.now()}")

from twilio.rest import Client
import schedule
import time
import random
from dotenv import load_dotenv
import os
#Estos son los seis renglones que agregué hoy 25 de septiembre
import os

print("📋 Variables de entorno detectadas en Render:")
print("TWILIO_ACCOUNT_SID:", os.getenv("TWILIO_ACCOUNT_SID"))
print("TWILIO_AUTH_TOKEN:", os.getenv("TWILIO_AUTH_TOKEN"))
print("TWILIO_WHATSAPP_NUMBER:", os.getenv("TWILIO_WHATSAPP_NUMBER"))
print("TO_WHATSAPP_NUMBER:", os.getenv("TO_WHATSAPP_NUMBER"))


# Cargar variables de entorno desde .env
load_dotenv()

# Leer las credenciales
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')

lista_numeros = [
    'whatsapp:+573004011292',  # Tu número
    #'whatsapp:+573005997275',  # Isnardo
    #'whatsapp:+573133120839',  # Alfonso
    #'whatsapp:+573013703799',  # Hermes
    #'whatsapp:+573219159178',  # José Moreno
    #'whatsapp:+573193313819',  # Andrés
    #'whatsapp:+573125593931', # Marylú
    'whatsapp:+573132744436', #CAR
]

# Crear cliente de Twilio
print(f"SID: {account_sid}")
print(f"Token: {auth_token[:6]}...")  # No mostramos todo por seguridad
print(f"Números a enviar: {lista_numeros}")
client = Client(account_sid, auth_token)

# Función para enviar mensaje aleatorio desde el archivo
def enviar_recordatorio():
    try:
        with open("mensajes.txt", "r", encoding="utf-8") as file:
            mensajes = [line.strip() for line in file if line.strip()]
        
        if not mensajes:
            print("⚠️ El archivo 'mensajes.txt' está vacío.")
            return

        mensaje = random.choice(mensajes)

        for numero in lista_numeros:
            message = client.messages.create(
                from_=from_whatsapp_number,
                body=mensaje,
                to=numero
            )
            print(f"✅ Mensaje enviado a {numero}. SID: {message.sid}")

    except Exception as e:
        print(f"❌ Error al enviar el mensaje: {e}")

# Programar el envío cada hora (puedes cambiar a every(1).minutes para probar)
#schedule.every().hour.do(enviar_recordatorio)
schedule.every().day.at("10:22").do(enviar_recordatorio)

#schedule.every(1).hora.do(enviar_recordatorio)
# schedule.every(1).minutes.do(enviar_recordatorio)  # Descomenta para pruebas rápidas

print("⏳ Bot activo. Enviando recordatorios a las 10:22 horas...")

# Mantener el bot activo
while True:
    schedule.run_pending()
    time.sleep(10)  
    
    """
    
    
# =========================
# Nuevo código listo para Render
# =========================
import os
from twilio.rest import Client
from datetime import datetime

# =========================
# Carga de variables de entorno
# =========================
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_WHATSAPP_NUMBER")
to_number = os.getenv("TO_WHATSAPP_NUMBER")

# =========================
# Verificación de variables
# =========================
if not all([account_sid, auth_token, twilio_number, to_number]):
    raise ValueError("❌ Error: Alguna variable de entorno no está definida correctamente.")

print(f"✅ Variables de entorno cargadas correctamente. SID: {account_sid[:6]}...")

# =========================
# Inicialización del bot
# =========================
print(f"🚀 Bot iniciado en Render a las {datetime.now()}")

# =========================
# Envío de mensaje de prueba
# =========================
try:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="🚀 Mensaje de prueba desde Render",
        from_=f"whatsapp:{twilio_number}",
        to=f"whatsapp:{to_number}"
    )
    print(f"✅ Mensaje enviado correctamente. SID: {message.sid[:6]}...")
except Exception as e:
    print(f"❌ Error al enviar mensaje: {e}")

# =========================
# Aquí podrías seguir con tu lógica de recordatorios programados
# =========================

"""
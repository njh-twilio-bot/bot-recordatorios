# =========================
# Bot de recordatorios con Twilio + Render
# Última depuración: septiembre 26
# =========================

import os
import datetime
import schedule
import time
import random
from twilio.rest import Client
from dotenv import load_dotenv

# =========================
# 1. Cargar variables de entorno
# =========================
load_dotenv()  # Render inyecta las variables, pero lo dejamos por compatibilidad local

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Lista de destinatarios
lista_numeros = [
    'whatsapp:+573004011292',  # Tu número
    'whatsapp:+573132744436',  # CAR
]

# =========================
# 2. Verificación de variables
# =========================
print(f"🚀 Bot iniciado en Render a las {datetime.datetime.now()}")
print("📋 Variables de entorno detectadas en Render:")
print("TWILIO_ACCOUNT_SID:", account_sid[:6] + "..." if account_sid else None)
print("TWILIO_AUTH_TOKEN:", auth_token[:6] + "..." if auth_token else None)
print("TWILIO_WHATSAPP_NUMBER:", from_whatsapp_number)
print("Lista de números destino:", lista_numeros)

if not all([account_sid, auth_token, from_whatsapp_number]):
    raise ValueError("❌ Error: Falta alguna variable de entorno obligatoria.")

# =========================
# 3. Cliente Twilio
# =========================
client = Client(account_sid, auth_token)

# =========================
# 4. Función para enviar recordatorio
# =========================
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
            print(f"✅ Mensaje enviado a {numero}. SID: {message.sid[:6]}...")

    except Exception as e:
        print(f"❌ Error al enviar el mensaje: {e}")

# =========================
# 5. Programación de tareas
# =========================
# Para pruebas rápidas: cada minuto
# schedule.every(1).minutes.do(enviar_recordatorio)

# Para producción: a las 00:53
schedule.every().day.at("00:53").do(enviar_recordatorio)

print("⏳ Bot activo. Enviará recordatorios a la hora programada...")

# =========================
# 6. Mantener el bot corriendo
# =========================
while True:
    schedule.run_pending()
    time.sleep(10)

from twilio.rest import Client
import schedule
import time
import random
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Leer las credenciales
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')

lista_numeros = [
    'whatsapp:+573004011292',  # Tu número
    'whatsapp:+573005997275',  # Isnardo
    'whatsapp:+573133120839',  # Alfonso
    'whatsapp:+573013703799',  # Hermes
    'whatsapp:+573219159178',  # José Moreno
    'whatsapp:+573193313819',  # Andrés
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
schedule.every().day.at("19:00").do(enviar_recordatorio)

#schedule.every(1).hora.do(enviar_recordatorio)
# schedule.every(1).minutes.do(enviar_recordatorio)  # Descomenta para pruebas rápidas

print("⏳ Bot activo. Enviando recordatorios a las 19:00 horas...")

# Mantener el bot activo
while True:
    schedule.run_pending()
    time.sleep(10)

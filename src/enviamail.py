#!/usr/bin/python
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import src.funciones as fun
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


def validMail(receptor):
    while True:
        regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if(re.search(regex,receptor)):  
            return receptor.lower()  
        else:  
            show = "La dirección no es válida. Tienes el reporte en PDF en la carpeta del proyecto."
            raise ValueError(show)

def enviaMail():
    """configurando correo"""
    key = os.getenv("pass")
    message = MIMEMultipart('alternative')
    message['Subject'] = 'Reporte de producción de alimentos'
    message['From'] = 'acorelldeveloper@gmail.com'
    message['To'] = 'agalvezcorell@gmail.com'
    receptor = input(str("Introduce el e-mail donde quieres enviar el reporte: "))
    validMail(receptor)

    # PARA ENVIAR EL ARCHIVO ADJUNTO
    nombre_adjunto = "Reporte"
    archivo_adjunto = open("archivo.pdf", 'rb')
    # Creamos un objeto MIME base
    message.attach(MIMEText('Adjunto el reporte con la producción de alimentos solicitados en el año solicitado', 'plain'))
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    #Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', f"attachment; filename= {nombre_adjunto}.pdf",)
    # Y finalmente lo agregamos al mensaje
    message.attach(adjunto_MIME)
    text = message.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('acorelldeveloper@gmail.com', f'{key}')
    server.sendmail('acorelldeveloper@gmail.com', f'{receptor}', text)
    server.quit()
    
import smtplib

from email.mime.text import MIMEText

msg = MIMEText("¡Este es un correo falsificado!")
msg['Subject'] = 'Prueba de spoofing'
msg['From'] = 'presidente@dominio.com'
msg['To'] = 'destinatario@mailhog.local'

with smtplib.SMTP('localhost', 1025) as server:
    server.sendmail('presidente@dominio.com', ['destinatario@mailhog.local'], msg.as_string())

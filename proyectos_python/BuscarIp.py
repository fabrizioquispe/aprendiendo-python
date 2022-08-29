"Encontrar Ip y Nombre del Ordenador, El modulo socket sirve para traer información de la comunicacion en la red"
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(hostname)
print(ip)
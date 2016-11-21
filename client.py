#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Dirección IP y puerto del servidor pasada por comandos.
try:
    METHOD = str(sys.argv[1])
    RECEIVER = str(sys.argv[2])
except:
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")

SERVER = 'localhost'
chops = RECEIVER.split('@')
LOGIN = chops[0]
IP = chops[1][:-5]
PORT = int(chops[1][-4:])

# Contenido que vamos a enviar
LINE = str(METHOD + ' sip:' + LOGIN + '@' + IP + ' SIP/2.0\r\n')

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)
print('Recibido -- ', data.decode('utf-8'))

if METHOD == 'INVITE':
    ACKLINE = str('ACK' + ' sip:' + LOGIN + '@' + IP + ' SIP/2.0\r\n')
    print("Enviando: " + ACKLINE)
    my_socket.send(bytes(ACKLINE, 'utf-8') + b'\r\n')

elif METHOD == 'BYE':

    print("Terminando socket...")
    # Cerramos todo
    my_socket.close()
    print("Fin.")

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion\r\n\r\n")

        # Leyendo línea a línea lo que nos envía el cliente
        line = self.rfile.read()
        data = line.decode('utf-8')
        chops = data.split(' ')
        print("El cliente nos manda: " + line.decode('utf-8'))
        
        if chops[0] == 'INVITE':
            self.wfile.write(b"SIP/2.0 100 Trying\r\n\r\n")
            self.wfile.write(b"SIP/2.0 180 Ring\r\n\r\n")

        if chops[0] == 'ACK':
            pass
        
        if chops[0] == 'BYE':
            pass
                
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    
    PORT = int(sys.argv[2])
    serv = socketserver.UDPServer(('', PORT), EchoHandler)
    print("Listening...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Finalizado servidor")

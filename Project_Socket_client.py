#Proyecto para el modulo de Redes
#Lectura de temperatura y presion del Sparkfun weather shield

'''
    socket cliente tipo UDP

'''

import Adafruit_CharLCD as LCD
import socket
import time
import sys
import os

#Este primer socket TCP ayudara a encontrar al HOST
#mediante un while e ir sumando 1 a la direccion IP
#hasta encontrar al sevidor

s = socket.socket()
direccion  = '192.168.15.' #datos de la IP sin cambiar
direccion2 = 2		    #aqui comenzaremos a sumar desde la direccion 2 hasta la 255
HOST = direccion + str(direccion2)#Union para crear una IP para el socket
PUERTO = 8888
print '---Buscando IP del servidor---'

while True:
    try:
	if s.connect((HOST, PUERTO)) == False: #AL no hallar respuesta del servidor se leerá como un false
	#Si a IP no es la del servidor, cierra el socket y comienza una nueva busqueda
	#una direccion arriba
		s.close()
	else:
		pass
    except:
	print HOST + ' X'
	direccion2 = int(direccion2) + 1
	HOST = direccion + str(direccion2)
    else:
	break

s.close()

#Ya una vez encontrado el HOST del servidor se cra un nuevo soket UDP
#Para el recibimiento de datos para su impresion en el lcd 1x2

print 'Servidor encontrado: ' + HOST

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

host = HOST;
port = 8888;

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

# Pinos LCD x Raspberry (GPIO)
lcd_rs     = 18
lcd_en     = 23
lcd_d4     = 12
lcd_d5     = 16
lcd_d6     = 20
lcd_d7     = 21
lcd_brillo = 4

# Define numero de caracteres y de lineas
lcd_carac = 16
lcd_linea = 2

# Inicializa o LCD nos pinos configurados acima
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                           lcd_d7, lcd_carac, lcd_linea, lcd_brillo)
 
print 'Recibiendo datos del Servidor'

while(1) :
    try :
	msg = 'Temperatura y presion'
        #Set the whole string
	s.sendto(msg, (host, port))

	lcd.clear()
         
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
#	print 'Recibiendo datos del Servidor'
	print ' Temp.    Presion'         
	print  reply

        # Imprime texto en la primera linea
        lcd.message('Temp C  Pres KPa\n')

        # Imprime texto en la segunda linea
	lcd.message( reply + '\n')
        time.sleep(1)

        #Imprime texto en la primera linea
        lcd.message('           \n')

        #Imprime texto en la primera linea
        lcd.message('... Sensando ...\n')
        time.sleep(1)

    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

s.close()


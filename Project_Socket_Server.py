'''
    Simple udp socket server
'''
 
import socket
import sys
import Adafruit_CharLCD as LCD
import os
import time
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket Creado Correctamente'
except socket.error, msg :
    print 'Fallo la connexion con el socket. Error : ' + str(msg[0]) + ' Mensaje ' + msg[1]
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
 
# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket Enlazado'
 
#now keep talking with the client

while 1:

    lcd.clear()
    
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
     
    if not data: 
        break
    
    msg = data.strip()
    print 'Mensaje recibido: ' + msg
    
    # Imprime texto en la primera linea
    lcd.message('Temp C  Pres KPa\n')

    # Imprime texto en la segunda linea
    lcd.message( msg + '\n')

    time.sleep(1)

    #Imprime texto en la primera linea
    lcd.message('           \n')

    #Imprime texto en la primera linea
    lcd.message('  Sensando....\n')

    time.sleep(1)

s.close()


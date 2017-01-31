'''
     socket server tipo UDP
'''
 import socket
import smbus
import time
import sys

#Este primer socket es el encargador de ayudar a dar su direccion IP
#al cliente para despues comenzar a envir los datos
 
HOST = ''   
PORT = 8888 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
s.listen(10)
conn, addr = s.accept()
s.close

#-----------------------------------------------
#Comienza el sensado de la presion y temperatura
#Para enviarlos al cliente que los solicite

HOST = ''   
PORT = 8888 
 
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket creado'
except socket.error, msg :
    print 'Fallo creacion del Socket. Error de codigo : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Fallo el enlace. Error de codigo : ' + str(msg[0]) + ' Mensaje ' + msg[1]
    sys.exit()
     
print 'Socket enlazado'

print 'Inicia envio de datos al cliente'
 
while 1:

        bus = smbus.SMBus(1)
        bus.write_byte_data(0x60, 0x13, 0x07)
        time.sleep(1)
        data = bus.read_i2c_block_data(0x60, 0x00, 6)

        temp = ((data[4] * 256) + (data[5] & 0xF0)) / 16
        cTemp = temp / 16.0

        bus.write_byte_data(0x60, 0x26, 0x39)
        time.sleep(1)
        data = bus.read_i2c_block_data(0x60, 0x00, 4)

        pres = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
        pressure = (pres / 4.0) / 1000.0

        Celsius = str(cTemp)
        Pascal = str(pressure)

        msg = ' '+ Celsius[:5]+ '    ' +Pascal[:5]

	#Aqui eta el envio
        d = s.recvfrom(1024)
        data = d[0]
        addr = d[1]
     
        if not data: 
            break
     
	reply =  msg
	print ' Temp.    Presion'
	print msg
        s.sendto(reply , addr)
     
s.close()



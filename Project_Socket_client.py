#Proyecto para el modulo de Redes
#Lectura de temperatura y presion del Sparkfun weather shield

'''
    socket cliente tipo UDP

'''

import socket   #for sockets
import smbus
import time
import sys 	#for exit

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print "Error en la creacion"
    sys.exit()

host = '192.168.15.1';
port = 8888;

while 1:
	bus = smbus.SMBus(1)
	bus.write_byte_data(0x60, 0x26, 0xB9)
	bus.write_byte_data(0x60, 0x13, 0x07)
	bus.write_byte_data(0x60, 0x26, 0xB9)
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

	try :
        	s.sendto(msg, (host, port))
		print "Temperatura  : %.2f C" %cTemp
		print "Presion : %.2f KPa" %pressure
	except socket.error, msg:
	        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        	sys.exit()
s.close()


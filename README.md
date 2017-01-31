Proyecto STATION-X

El proyecto consiste en sensar la Temperatura y Presión mediante una Sparkfun Weather Shield (https://www.sparkfun.com/products/12081),
 el Servidor estará esperando a que un cliente, dentro del dominio de este, solicite los datos del sensado. El Cliente hará una búsqueda por cada
 IP del dominio donde se encuentra hasta hallar al servidor para establecer una comunicación. EL cliente al recibir los datos los imprimirá en
 una LCD 16x2.

<IMG src=https://github.com/chrisdeuce/socket/blob/master/Busqueda.png>

 Del lado izquierdo se encuentra nuestro cliente que comienza una búsqueda por cada IP cambiando la dirección de ultimo octeto, al no hallar
 respuesta a la solicitud cierra la conexión y comienza una nueva con la ip siguiente. Del lado derecho esta nuestro Servidor esperando a que
 un cliente se conecté a él, se muestra sombreado como su ip es la 192.168.15.99.

<IMG src=https://github.com/chrisdeuce/socket/blob/master/Datos.png>

 Del lado derecho vemos como el cliente encontró al servidor en la ip 192.168.15.99 y comienza a recibir los datos de Temperatura y presión para
 imprimirlos en la LCD 16x2.

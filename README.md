#Nombre del proyecto
Sistema distribuido de gestion de pedidos mediante el uso de las siguientes tecnologias:
-Flask
-MySql
-Kafka
-Nginx
-DOCKER
Cuenta con un dashboard web que filtra los pedidos por sucursal, ademas de estar ordenado por fechas
El consumer kafka lee los mensajes de pedidos del topic correspondiente, y almacena en la base MYSQL 
Posterior, el consumer mostrara los datos en el dashboard web mediante un docker creado
-Pendiente de pullir y probar fallos
-Pendiente de ordenar volumenes y contenedores
Logica actualizada 27/01/25 
-Pendiente organizacion de contenedores y borrar archivos no usados

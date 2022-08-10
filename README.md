                                                                        Proyecto Final: Aplicacion "gym"

El proyecto se trata de una aplicacion llamada "gym" para el administrador de un gimnasio. En la misma existen 3 modelos: Actividades, Socios y Planes. En cada modelo se pueden agregar nuevos datos y buscar datos.
Para acceder a la app hay que ir a la url: http://127.0.0.1:8000/gym/inicio

1- Actividades:
Las actividades estan definidas por nombre, dia, horario y cupo. 
Para ver las actividades disponibles, se debe acceder desde el inicio haciendo click en el link "Actividades" o a traves de la url http://127.0.0.1:8000/gym/actividades 
Para buscar actividades, la busqueda se realiza llenando el campo nombre y pulsando el boton "Buscar". 
- si la actividad existe, o existe alguna actividad cuyo nombre contenga lo escrito, la muestra debajo del formulario de busqueda;
- si la actividad no existe, no devuelve nada.
Para hacer otra busqueda, hay que volver a pulsar el boton "Buscar". 
Para agregar una nueva actividad se debe ir a la url http://127.0.0.1:8000/gym/actividades/agregar, llenar todos los campos definidos (nombre, dia, horario, cupo) y pulsar el boton "Agregar". Esta accion te devuelve a la pagina de Inicio.
Para chequear que se haya cargado la nueva actividad, hacer click en el link "Actividades" del Inicio o a traves de la url http://127.0.0.1:8000/gym/actividades
Para agregar otra actividad, hay que volver a ingresar a la url http://127.0.0.1:8000/gym/actividades/agregar y repetir el prodedimiento.

2- Socios:
Los socios estan definidos por nombre, apellido, email y si pago o no la cuota.
Para ver los socios inscriptos, se debe acceder desde el inicio haciendo click en el link "Socios" o a traves de la url http://127.0.0.1:8000/gym/socios
Para buscar socios, la busqueda se realiza llenando el campo apellido y pulsando el boton "Buscar".
- si el socio existe, o existe algun socio cuyo apellido contenga lo escrito, lo muestra debajo del formulario de busqueda;
- si el socio no existe, no devuelve nada.
Para hacer otra busqueda, hay que volver a pulsar el boton "Buscar". 
Para agregar un nuevo socio se debe ir a la url http://127.0.0.1:8000/gym/socios/agregar, llenar todos los campos definidos (nombre, apellido, email, pago cuota o no) y pulsar el boton "Agregar". Esta accion te devuelve a la pagina de Inicio.
Para chequear que se haya cargado el nuevo socio, hacer click en el link "Socios" del Inicio o a traves de la url http://127.0.0.1:8000/gym/socios
Para agregar otro socio, hay que volver a ingresar a la url http://127.0.0.1:8000/gym/socios/agregar y repetir el prodedimiento.

3- Planes:
Los planes estan definidos por nombre, cantidad de clases y precio. 
Para ver los planes disponibles, se debe acceder desde el inicio haciendo click en el link "Planes" o a traves de la url  http://127.0.0.1:8000/gym/planes
Para buscar planes, la busqueda se realiza llenando el campo cantidad_clases y pulsando el boton "Buscar".
- si la cantidad de clases existe, o existe algun plan cuya cantidad de clases contenga lo escrito, lo muestra debajo del formulario de busqueda;
- si la cantidad de clases no existe, no devuelve nada.
Para hacer otra busqueda, hay que volver a pulsar el boton "Buscar". 
Para agregar un nuevo plan se debe ir a la url http://127.0.0.1:8000/gym/planes/agregar, llenar todos los campos definidos (nombre, cantidad de clases, precio) y pulsar el boton "Agregar". Esta accion te devuelve a la pagina de Inicio.
Para chequear que se haya cargado el nuevo plan, hacer click en el link "Planes" del Inicio o a traves de la url http://127.0.0.1:8000/gym/planes
Para agregar otro plan, hay que volver a ingresar a la url http://127.0.0.1:8000/gym/planes/agregar y repetir el prodedimiento.
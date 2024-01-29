# Crear web similar a un blog

- Se deberá de manera individual. Crearás una aplicación web estilo blog programada en Python en Django. Esta web tendrá admin, perfiles, registró, páginas y formularios.

- La entrega se realizará enviando el link a GitHub, en el readme de Github deberá estar el nombre completo de los participantes y una descripción de dos o tres renglones contando qué hizo cada uno.

- En el github debe haber un video o link a vídeo donde nos muestran su web funcionando en no más de diez minutos.

- Dentro del Github deberá existir una carpeta con por lo menos 3 casos de pruebas debidamente documentados.

- Contar con algún acceso visible a la vista de "Acerca de mí" donde se contará acerca de los dueños de la página manejado en el route about/.  (En castellano un “acerca de mí” que hable un poco de los creadores de la web y del proyecto).

- Contar con algún acceso visible a la vista de blogs que debe alojarse en el route pages/. (Es decir un html que permite listar todos los blogs de la BD, con una información mínima de dicho blog).

- Acceder a una pantalla que contendrá las páginas. Al clickear en “Leer más” debe navegar al detalle de la page mediante un route pages/<pageId>. (O sea al hacer click se ve más detalle de lo que se veía en el apartado anterior).

- Si no existe ninguna página mostrar un "No hay páginas aún". (Aclarando, si en la página hacemos clic en algún lugar que no existe que diga eso, o que lleve a un html con esos mensaje, no dejar botones que no responden).

- Para crear, editar o borrar las fotos debes estar registrado como Administrador.

- Cada blog, es decir cada model Blog debe tener como mínimo, un título, subtítulo, cuerpo, autor, fecha y una imagen (mínimo y obligatorio, puede tener más).

- Si los estudiantes deciden resolverlo de manera grupal, deben avisar al tutor y enviarle los nombres de los estudiantes que conforman el grupo de trabajo. Luego, agregar una carátula o instancia en el PF con los nombres de los estudiantes.

- Requisitos para el Proyecto final (Pages es un Modelo de ejemplo): 

Home
About (acerca de mi)
Login
Signup
Logout
Update profile
Avatar

Pages (1+ MODEL)
Search pages
Search pages - results

CRUD Completo Model (1+)
Create page
Read page
Update page
Delete page

## Requisitos base

- Tener una app de registro donde se puedan registrar usuarios en el route accounts/signup, un usuario está compuesto por: email - contraseña - nombre de usuario.

- Tener una app de login en el route accounts/login/ la cual permite loguearse con los datos de administrador o de usuario normal.

- Tener una app de perfiles en el route accounts/profile/ la cual muestra la info de nuestro usuario y permite poder modificar y/o borrar: imagen - nombre - descripción -  un link a una página web - email y contraseña.

- Contar con un admin en route admin/ donde se puedan manejar las apps y los datos en las apps.

- Tener una app de mensajería en el route messages/ para que los perfiles se puedan contactar entre sí.

NOTA: No hace falta que sean APPs separadas, con dos APP estarán bien.

Recuerden que en la clase 1 tienen disponible un proyecto modelo de un ex estudiante para tomar como inspiración.

## Duda frecuente

En caso que no quieras hacer una Web simil Blog, puedes optar por otra opción, pero deberá tener la misma estructura que el modelo básico, título, subtítulo, texto, imagen/es, autor, fecha. Y la web debe tener un funcionamiento similar. 

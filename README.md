# Projecto-Final-Miguel/Alvarez

Introduccion: 
-El trabajo fue hecho en base a la pre entrega de Lautaro Miguel, ya que nos parecio bien a los dos seguir con su idea del e-commers. 
-Como gran parte ya estaba hecho, decidimos que Lautaro Miguel se encargue de agregar los modelos y productos faltantes con sus respectivas views y urls.
-Mientras que Lautaro Alvarez se encargo de todo lo que involucre users, login, register y demas. 

Lautaro Alvarez se encargo de las apps Users y Blog,
Lautaro Miguel se encargo de las apps Tienda y Pagina

Lautaro Alvarez: 

Users: (creacion de app, views, models, forms y templates)

1.1- Login
     -A traves del boton "login" del navbar o con el comando "users/login". Aqui debera poner su nombre de usuario y su contraseña para poder loguearse. 

1.2- Register
    -A traves del boton "register" del navbar o con el comando "users/register". Este formulario cuenta con un usuario, contraseña y un email.

1.3- Logout  
    -Si el usuario ya se encuentra registrado y logueado, le aparecera el boton "logout" en el navbar o a traves del comando "users/logout". Al seleccionar esta opcion,
    lo llevara a un template que dira "cerraste sesion"
    
1.4- Profile
   -Si el usuario ya esta registrado y logueado, le aparecera el boton "profile" en el navbar o a traves del comando "users/my-profile". Dentro del mismo podra editar su
   perfil como asi tambien eliminarlo.
   
2- Restricciones de superuser:
-Solo los usuarios admin o superusers tendran el acceso a la edicion y borrado de productos
-Solo los usuarios registrados y logueados tendran acceso al e-commers, con excepcion de la seccion "about us"

3- About us (apps de blog, template, views, models)
-Breve descripcion de los integrantes y el proyecto
-No hace falta ser usuario para ingresar

4- Creacion de Readme



Lautaro Miguel:

Tienda (creacion de app, models, views, forms y templates)

1 List products
   -Pagina principal donde se ve el listado de todos los productos de la base de datos. Con la posibilidad de editar y borrar (solo admin) y tambien ver los detalles
   del mismo (cualquier usuario).
   -Contamos con Peripherals, Games, Consols y Phones
   
2 Create 
  -Mediante el comando "create-..." se podran crear nuevos productos a traves de un formulario. Pueden ser Peripherals, Games, Consols y Phones

3 Delete 
  -Mediante el comando "delete-..." se podran eliminar cualquiera de los productos o con el boton "delete" que hay en ellos. Pueden ser Peripherals, Games, Consols y Phones
  
4 Update 
 -Mediante el comando "Update-..." se podran editar los productos.Pueden ser Peripherals, Games, Consols y Phones
 
5 Read
 -Mediante el comando "Detail-..." se podran ver en detalle las caracteristicas de los productos. Pueden ser Peripherals, Games, Consols y Phones
 

 
Creacion del video demostrativo del proyecto: https://www.youtube.com/watch?v=AvixDpu-weY



A tener en cuenta: 
Tuvimos un pequeño inconveniente en la parte de "profile". Cuando queremos editar los campos del perfil del usuario, nos deja pero no pudimos hacer que guarde el 
nombre de usuario que ponemos.
Si se accede con un usuario normal, al acceder al profile no carga los datos. 

superuser: 
usuario: Miguel
contraseña: lautaromiguel

usuario normal: 
usuario: JuanCarlos
contraseña: pepito123
   
   
    

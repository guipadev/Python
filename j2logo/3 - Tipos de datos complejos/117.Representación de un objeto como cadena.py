Representaci�n de un objeto como cadena
Una singularidad de la clase str es que a su constructor se le puede pasar cualquier objeto. Al hacer esto, la funci�n str() devuelve la representaci�n en forma de cadena de caracteres del propio objeto (si se pasa un string devuelve el string en s�).

Normalmente, al llamar a la funci�n str(objeto) lo que se hace internamente es llamar al m�todo __str__() del objeto. Si este m�todo no existe, entonces devuelve el resultado de invocar a repr(objeto).
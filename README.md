# Proyecto Urban Grocers
### crear un kit 

##### pasos: 
1- Crear un usuario 
2- Crear un kit 
3- Realizar pruebas positivas y negativas al campo "name" del cuerpo del kit 

##### Archivos:
* Configuration.py 
* data.py
* sender_stand_resquets.py
* create_kit_name_test.py
* gitignore

##### funciones declaradas Archivo configuration.py
1- Para crear un usuario: def post_new_user(body):
2- Para recibir el token : def get_new_user_token():
3- Para crear un kit: def post_new_client_kit(kit_body):

##### funciones declaradas Archivo create_kit_name_test.py
1- Para probar el campo name: def get_kit_body(name):
2- Funcion positiva: def positive_assert(name):
3- Funcion negativa: def negative_assert(name):
4- Funcion negativa para la prueba 8: def negative_assert_no_name(name):

##### Pruebas realizadas en el archivo create_kit_name_test.py

1-	El número permitido de caracteres (1): 
kit_body = { "name": "a"}	Código de respuesta: 201 

2-	El número permitido de caracteres (511): 
kit_body = {aaaaaa....}	Código de respuesta: 201 

3-	El número de caracteres es menor que la cantidad permitida (0):
kit_body = { "name": "" }	Código de respuesta: 400

4-	El número de caracteres es mayor que la cantidad permitida (512):
kit_body = { "aaaaa.....” }	Código de respuesta: 400

5-	Se permiten caracteres especiales:
kit_body = { "name": ""№%@"," }	Código de respuesta: 201 

6-	Se permiten espacios:
kit_body = { "name": " A Aaa " }	Código de respuesta: 201 

7-	Se permiten números:
kit_body = { "name": "123" }	Código de respuesta: 201 

8-	El parámetro no se pasa en la solicitud:
kit_body = { }	Código de respuesta: 400

9-	Se ha pasado un tipo de parámetro diferente (número): 
kit_body = { "name": 123 }	Código de respuesta: 400
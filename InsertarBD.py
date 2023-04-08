from print final import final
import mysql.connector
from mysql.connector import errorcode

DB_HOST = '3306' # dirección IP donde está montada la base de datos
DB_USER = 'root' # usuario válido para conectarse a la base de datos
DB_PASS = 'saocro45' # contraseña que se tengan en el PC donde reside la base de datos
DB_NAME = 'peticioncambio '  # nombre de la base de datos a donde se quiere uno conectar
try:
    miconexion = mysql.connector.connect(user=DB_USER, password=DB_PASS,host=DB_HOST,database=DB_NAME)  # Conectar a la base de datos
    cursor = miconexion.cursor()  # Crear un cursor
    proyecto = input ("nombre de tu proyecto ")
    numero = input ("su numero: ")
    solicitante = input ("porque solicitas el cambio")
    fecha = input ("a que dia nos encontramos ")
    cambiosolicitud= input("razones por las que deseas la solicitud de cambio")
    analizadorcambio= input("quien es el encargado de analizar la solicitud de cambio")
    prioridadcambio= input("cual es la prioridad del cambio")
    valoracioncambio= input ("de cuanto es la valoracion del cambio")
    implementacioncambio= input("como se implementaria el cambio ")
    esfuerzo_estimado= input("cuanto tiempo te tardarias en implementar estos cambios")
    fecha_equipo= input ("cuando tu equipo tendria el cambio")
    fecha_decision= input("cuando se realizo la decision del cambio")
    decision= input(" que decision fue la que se tomo para realizar el cambio ")
    implementador_cambio= input("quien es el encargado de implementar el cambio")
    fecha_decambio = input("cuando se empezaria el cambio")
    fecha_envioQA= input("cuando se le enviaria al QA ")
    decisionQA= input("que decidio el QA para poder realizar el cambio")
    fecha_envioCM= input("cuando estara listo")
    comentarios= input("comentarios")

# riesgo de inyección sql
 #   query = "INSERT into malumno (bol_alu, app_alu, apm_alu, nom_alu, dir_alu, sex_alu) " \
          # "values ('"+boleta+"', '"+app+"', '"+apm+"', '"+nombre+"', '"+dir+"','"+sex+"')"

    query = "INSERT into malumno (proyecto, numero, solicitante, fecha,cambiosolicitud,analizadorcambio,prioridadcambio,valoracioncambio,implementacioncambio,esfuerzo_estimado, fecha_equipo, fecha_decision, decision, implementador_cambio,fecha_decambio,fecha_envioQA,decisionQA,fecha_envioCM, comentarios )"/
            "values (%s, %s, %s, %s ,%s,%s,%S,%s,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S)"
    valores = (proyecto, numero, solicitante, fecha, cambiosolicitud, analizadorcambio, prioridadcambio, valoracioncambio,implementacioncambio,esfuerzo_estimado, fecha_equipo, fecha_decision, decision, implementador_cambio,fecha_decambio,fecha_envioQA, decisionQA,fecha_envioCM,comentarios)
    try:
        # Ejecutamos el comando
        cursor.execute(query, valores)
        # Efectuamos los cambios en la base de datos
        miconexion.commit()
        print(cursor.rowcount, "Registro Agregado Satisfactoriamente")
    except:
        # Si se genero algun error revertimos la operación
        miconexion.rollback()
        print("La transacción no fue llevada a cabo")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error con el usuario o password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de datos no existe")
    else:
        print(err)
finally:
    print("Se cerró la conexión a la base de datos")
    cursor.close()  # Cerrar el cursor
    miconexion.close()  # Cerrar la conexión
print(final)

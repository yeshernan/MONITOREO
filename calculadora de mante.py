print("BIENVENIDO, calcularemos el costo de mantenimento, reingenieria y beneficiero ")
P1=int(input("Cual es el costo de mantenimiento actual de su software:"))
P2=int(input("Cual es el costo de operacion actual de su software:"))
P3=int(input("El valor empresarial actual de tu software:"))
L= int(input("cuanto es tu tiempo estimado de vida para tu software:"))

costomantenimiento=(P3-(P1+P2))*L

print("EL NUEVO COSTO DE MANTENIMIENTO DE TU SOFTWARE ES EL SIGUIENTE: ")
print(costomantenimiento)

print("AHORA CALCULAREMOS EL COSTO DE LA REINGENIERIA Y EL COSTO BENEFICIARIO")

P4=int(input("Cual es el costo de mantenimiento despues de la reingenieria:"))
P5=int(input("Cual es el costo de operacion actual despues de la reingenieria:"))
P6=int(input("El valor empresarial despues de la reingenieria:"))
P7=int(input("Cual es el costo de la reingenieria:"))
P8=int(input("Cual es el tiempo de la reingenieria:"))
P9=1

Reingenieriacost= P6-(P4+P5)*(L-P8)-(P7*P9)
Beneficiariocost= P7-P4

print("EL COSTO TOTAL DE LA REINGENIERIA Y EL BENEFICIARO SERIA UN TOTAL DE :")
print(Reingenieriacost)
print(Beneficiariocost)


TOTAL=costomantenimiento+Reingenieriacost+Beneficiariocost

print("EL TOTAL, EL MANTENIMIENTO DE TU SOFTWARE SALDIRA EN:")
print(TOTAL)

print("GRACIAS POR USAR NUESTRO SISTEMA Y SUERTE PARA PAGAR EL MANTENIMIENTO")
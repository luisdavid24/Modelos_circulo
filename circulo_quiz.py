import random
import math

mi_circulo = [0,1,2,3,4,5,6,7]
vector_pasos=[]

#Se busca obtener el nuevo índice que hace referencia a un número adyacente al número inicial.
#Esto se logra mediante random.randint(1, 2). 
#Si sale un dos, se avanza en las manecillas del reloj; 
# si sale un uno, se avanza en contra de las manecillas del reloj.
def condiciones(indece_circulo):
    numero_aleatorio = random.randint(1,2)  
    if(numero_aleatorio==2):
        if(indece_circulo==7):
            indece_circulo=0
        else:
            indece_circulo+=1
    else:
        if(indece_circulo==0):
            indece_circulo=7
        else:
            indece_circulo-=1
    return indece_circulo


#Ahora, se busca obtener el número de pasos necesarios para volver al punto de partida, 
#es decir, al número cero. Esto se logra a través de un ciclo 
#while que iterará hasta encontrar el cero, 
#registrando el número de pasos en un vector.
def buscar():
    indece_circulo=0
    numero_pasos=0
    numero_circulo=mi_circulo[0]
    encontrar=False
    while encontrar==False:
        numero_pasos+=1
        indece_circulo=condiciones(indece_circulo)
        numero_circulo=mi_circulo[indece_circulo]
        if(numero_circulo==0 ):
            encontrar=True
    return numero_pasos

#Ahora, se busca obtener el número de pasos necesarios para volver al punto de partida,
#es decir, al número cero.Esto se logra a través de un ciclo for que iterará hasta encontrar el cero, 
#registrando el número de pasos en un vector.
for iteracion in range(1, 100):
    vector_pasos.append(buscar())
    


vector_pasos.sort()
longitud = len(vector_pasos)
media = sum(vector_pasos) / longitud
valor_minimo=vector_pasos[0]
valor_maximo=vector_pasos[longitud-1]

if longitud % 2 == 1:
    numero_medio = vector_pasos[longitud // 2]
else:
    numero_medio = (vector_pasos[longitud // 2 - 1] + vector_pasos[longitud // 2]) / 2

suma_cuadrados_diferencias = sum((x - media) ** 2 for x in vector_pasos)
varianza = suma_cuadrados_diferencias / len(vector_pasos)
desviacion_estandar = math.sqrt(varianza)

print("El número medio es:       ", numero_medio)
print("La media es:              ", media)
print("La desviación estándar es:", desviacion_estandar)
print("El valor minimo:          ", valor_minimo)
print("El valor maximo:          ", valor_maximo)






import random
import math

MI_CIRCULO = [0,1,2,3,4,5,6,7]
VECTOR_PASOS=[]

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
    numero_circulo=MI_CIRCULO[0]
    encontrar=False
    while encontrar==False:
        numero_pasos+=1
        indece_circulo=condiciones(indece_circulo)
        numero_circulo=MI_CIRCULO[indece_circulo]
        if(numero_circulo==0 ):
            encontrar=True
    return numero_pasos

#Ahora, se busca obtener el número de pasos necesarios para volver al punto de partida,
#es decir, al número cero.Esto se logra a través de un ciclo for que iterará hasta encontrar el cero, 
#registrando el número de pasos en un vector.
NUMERO_ITERACIONES=100
for iteracion in range(1,NUMERO_ITERACIONES):
    VECTOR_PASOS.append(buscar())
    


VECTOR_PASOS.sort()
longitud = len(VECTOR_PASOS)
media = sum(VECTOR_PASOS) / longitud
valor_minimo=VECTOR_PASOS[0]
valor_maximo=VECTOR_PASOS[longitud-1]

if longitud % 2 == 1:
    numero_medio = VECTOR_PASOS[longitud // 2]
else:
    numero_medio = (VECTOR_PASOS[longitud // 2 - 1] + VECTOR_PASOS[longitud // 2]) / 2

suma_cuadrados_diferencias = sum((x - media) ** 2 for x in VECTOR_PASOS)
varianza = suma_cuadrados_diferencias / len(VECTOR_PASOS)
desviacion_estandar = math.sqrt(varianza)

print("El número medio es:       ", numero_medio)
print("La media es:              ", media)
print("La desviación estándar es:", desviacion_estandar)
print("El valor minimo:          ", valor_minimo)
print("El valor maximo:          ", valor_maximo)






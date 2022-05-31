import numpy as np

personas = np.empty((2,0)) #Creo una matriz de 2 x 0 vacia

for i in range(5):
    nombre = input('Introduzca el nombre de la persona numero ' + str(i+1) +': ')
    edad = int(input('Intruduzca la edad de la persona ' + str(i+1) + ': '))
    personas = np.append(personas,np.array([[nombre],[edad]]), axis=1)

def indice(item):
    resultado = int(np.where(personas[1] == item)[0])
    return resultado

maximo = max(personas[1])
lugar = indice(maximo)
mayor = personas[:,lugar]

minimo = min(personas[1])
lugar = indice(minimo)
menor = personas[:,lugar]

print('El mayor es', mayor[0], 'y tiene', mayor[1],'años.')
print('El menor es', menor[0], 'y tiene', menor[1],'años.')


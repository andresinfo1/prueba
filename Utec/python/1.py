from array import array
import numpy as np

vector = np.array([10,9,8,7,6,5,4,3,2,1])

numero = int(input('Ingrese el numero a buscar: '))

lugar = np.where(vector == numero)
lugar_str = str(lugar[0])[1:-1] #En este método, convierte una lista en una cadena usando la función str() y luego elimina el primer y último carácter de esta cadena que son los corchetes.


if (lugar_str == ''):
    print ('\nEl numero no se encuentra en el vector')
else:    
    print(lugar[0])
    print ('\nEl numero se encuentra en el lugar: %s' %lugar_str)

vector.sort() #Este método ordena el vector de menor a mayor

print('\nEl vector ordenado queda de la siguiente forma: ', vector)




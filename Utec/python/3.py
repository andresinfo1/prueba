import numpy as np

personas = np.empty((2,0))

for i in range(5):
    nombre = input('Introduzca el nombre de la persona numero ' + str(i+1) +': ')
    edad = int(input('Intruduzca la edad de la persona ' + str(i+1) + ': '))
    personas = np.append(personas,[[nombre],[edad]], axis=1)

#personas = np.hstack([personas,(['luis'],[20])])

print(personas)
from pickle import FALSE, TRUE
import numpy as np
import random as rd
 
A = np.array([[2,1,0],[1,1,0],[0,0,1]])
B = np.array([[1,-1,0],[-1,2,0],[0,0,1]])

def inversa(A):
    ok = TRUE
    det = int(np.linalg.det(A)) #calculo el determinante de A
    if det != 0:
        inver = np.linalg.inv(A)
    else:
        ok = FALSE
    return(ok,inver)
 
def identidad():
    ident = np.empty([3, 3], dtype=int)
    for i in range(len(ident)):
        for j in range(len(ident[0])):
            if i == j: #and C[i][j] == 1:
                #count = count + 1
                ident[i][j] = 1
            else:
                ident[i][j] = 0  
    return(ident)
 
ident = identidad()
print(ident)


C = np.matmul(A,B) #Multiplicacion de las matrices anteriores
print('Matriz C\n %s' %C)


if np.array_equal(C,ident):
    print('hola %s'%C)
 
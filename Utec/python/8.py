#Ejercicio 8
capital_m = float(input('¿ Cuanto desea invertir por mes ? : '))
capital= capital_m
interes = 1
tiempo = 12
respuesta = 's'

def int_comp (cap):
    for i in range(tiempo-1):
        retorno = cap*(interes/100)
        cap = cap + retorno + capital_m
    return(cap)
    
while respuesta == 's':
    capital = int_comp(capital)
    print('El saldo de su inversion es $%.2f' %capital)
    respuesta = input('\n¿Desea calcular que el año siguiente se calcule sucesivamente? "s" "n": ').lower()
    if respuesta == 'n':
        break
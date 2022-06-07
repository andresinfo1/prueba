numero = 12
divisores = []

for i in range(1,numero+1):
    if numero % i == 0:
        divisores.append(i)

if len(divisores) > 2:
    print(str(divisores)[1:-1])
else:
    print('Es un numero primo')
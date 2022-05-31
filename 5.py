numero = 12
divisores = []

for i in range(1,numero+1):
    if numero % i == 0:
        divisores.append(i)

print(divisores)
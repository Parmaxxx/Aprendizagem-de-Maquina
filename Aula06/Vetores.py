limiar = 5

menores = []
maiores = []

for i in range(10):
    if(i< limiar):
        menores.append(i)
    elif (i> limiar):
        maiores.append(i)

print ('Resultado final')
print('Menores:', menores)
print('Maiores :', maiores)
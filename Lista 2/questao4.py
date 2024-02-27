nomes = ['Passat', 'Crossfox', 'DS5', 'C4', 'Jetta']
kms = [15000, 12000, 32000, 8000, 50000]


lista_nomes_km = list(zip(nomes, kms))


lista_veiculos_pouco_usados = []


for i in range(len(lista_nomes_km)):
   if lista_nomes_km[i][1] < 20000:
       lista_veiculos_pouco_usados.append(lista_nomes_km[i][0])


print(lista_veiculos_pouco_usados)

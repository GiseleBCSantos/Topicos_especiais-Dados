nomes = ['Passat', 'Crossfox', 'DS5', 'C4', 'Jetta']
kms = [15000, 12000, 32000, 8000, 50000]


dict_nomes_kms = {}


for i in range(len(nomes)):
   dict_nomes_kms[nomes[i]] = kms[i]


print(dict_nomes_kms)
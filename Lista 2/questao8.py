def main():
   dados = {
       'Crossfox': {'valor': 72000, 'ano': 2005},
       'DS5': {'valor': 125000, 'ano': 2015},
       'Fusca': {'valor': 150000, 'ano': 1976},
       'Jetta': {'valor': 88000, 'ano': 2010},
       'Passat': {'valor': 106000, 'ano': 1998}
   }


   verificar_fabricacao_veiculos(dados, 2000)




def verificar_fabricacao_veiculos(dictionary, year):
   cars = dictionary.keys()
   for car in cars:
       if dictionary[car]['ano'] >= year:
           print(car)




if __name__ == '__main__':
   main()

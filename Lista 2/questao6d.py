def main():
   dados = {
       'Passat': {
           'ano': 2012,
           'km': 50000,
           'valor': 75000,
           'acessorios': ['Airbag', 'ABS']
       },
       'Crossfox': {
           'ano': 2015,
           'km': 35000,
           'valor': 25000
       }
   }


   print(get_last_atribute(dados, 'Passat', 'acessorios'))




def get_last_atribute(dictonary, car, value):
   if car in dictonary:
       if value in dictonary[car]:
           car_values = dictonary[car][value]
           return get_last_item_list(car_values)
       else:
           return 'Não tem esse atributo no carro.'
   else:
       return 'Não temos esse carro'




def get_last_item_list(list):
   return list[len(list) -1]




if __name__ == '__main__':
   main()

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


   print(get_value(dados, 'Crossfox', 'valor'))




def get_value(dictionary,car, value):
   if car in dictionary:
       return dictionary[car][value]
   else:
       return 'Carro inserido não está no dicionário.'










if __name__ == '__main__':
   main()

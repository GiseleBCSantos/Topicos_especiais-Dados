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


   print(key_in_car(dados, 'acessorios', 'Crossfox'))




def key_in_car(dictonary, key, car):
   if car in dictonary:
       if key in dictonary[car]:
           return True
   return False




if __name__ == '__main__':
   main()

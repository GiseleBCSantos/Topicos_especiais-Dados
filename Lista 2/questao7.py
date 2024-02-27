def main():
   dados = {'Jetta': 88000, 'Crossfox': 72000, 'DS5': 124000}


   add_item(dados, 'Passat', 85000)
   add_item(dados, 'Fusca', 150000)


   print(dados)




def add_item(dictionary, key, value):
   dictionary[key] = value




if __name__ == '__main__':
   main()

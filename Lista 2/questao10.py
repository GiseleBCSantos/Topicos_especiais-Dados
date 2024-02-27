def main():
   dados = {
       'Crossfox': {'km': 35000, 'ano': 2005},
       'DS5': {'km': 17000, 'ano': 2015},
       'Fusca': {'km': 130000, 'ano': 1979},
       'Jetta': {'km': 56000, 'ano': 2011},
       'Passat': {'km': 62000, 'ano': 1999}
   }


   km_media(dados, 2019)




def km_media(dataset, ano_atual):
   for car in dataset:
       km_car = dataset[car]['km']
       km_med = km_car / (ano_atual - dataset[car]['ano'])
       print(round(km_med, 2))




if __name__ == '__main__':
   main()



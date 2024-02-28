import csv

class Terrorismo:
    def __init__(self, csv_file):
        self.csv_file = self.ler_arquivo(csv_file)

    def ler_arquivo(self, arquivo):
        list = []
        with open('terrorismo.csv', 'r') as csv_file:
            leitor_csv = csv.reader(csv_file)
            for i in leitor_csv:
                list.append(i)

        csv_file.close()

        return list


    def paises_com_mais_mortes_por_terrorismo(self):
        pais = ''
        mortes = 1

        for index, line in enumerate(self.csv_file):
            if line[3].isnumeric():
                if int(line[3]) > mortes:
                    mortes = int(line[3])
                    pais = line[0]

        print(f'Pais com mais mortes: {pais}\nQuantidade de mortes: {mortes}')



    def paises_com_mais_que_X_mortes_por_terrorismo(self, value):
        pais = ''
        mortes = 1

        for index, line in enumerate(self.csv_file):
            if line[3].isnumeric():
                if int(line[3]) > value:
                    mortes = int(line[3])
                    pais = line[0]
                    print(f"País: {pais}\nMortes: {mortes}\n------------------")


    def paises_com_americanos_mortos_por_terrorismo(self):
        pais = ''
        mortes = 0

        for index, line in enumerate(self.csv_file):
            if line[5].isnumeric():
                if int(line[5]) > 0:
                    mortes = line[5]
                    pais = line[0]

                    print(f"País: {pais}\nMortes: {mortes}\n------------------")

    def pais_maior_incidente_terrorismo(self):
        incidente = 0
        pais = ''

        for index, line in enumerate(self.csv_file):
            if line[1].isnumeric():
                if int(line[1]) > incidente:
                    incidente = int(line[1])
                    pais = line[0]

        print(f'Pais com mais incidentes: {pais}\nQuantidade de incidentes: {incidente}')


    def paises_com_mais_que_X_incidentes_terrorismo(self, value):
        incidente = 0
        pais = ''

        for index, line in enumerate(self.csv_file):
            if line[1].isnumeric():
                if int(line[1]) > value:
                    incidente = int(line[1])
                    pais = line[0]

                    print(f"País: {pais}\nIncidentes: {incidente}\n------------------")


# terrorismo = Terrorismo('terrorismo.csv')

# terrorismo.pais_com_mais_mortes_por_terrorismo()

# terrorismo.paises_com_mais_que_X_mortes_por_terrorismo(1000)

# terrorismo.paises_com_americanos_mortos_por_terrorismo()

# terrorismo.pais_maior_incidente_terrorismo()

# terrorismo.paises_com_mais_que_X_incidentes_terrorismo(100)
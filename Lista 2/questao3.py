carros = (
   (
   'Jetta Variant',
   'Motor 4.0 Turbo',
   2003,
   False,
   ('Rodas de liga', 'Travas elétricas', 'Piloto automático')
   ),
   (
   'Passat',
   'Motor Diesel',
   1991,
   True,
   ('Central multimídia', 'Teto panorâmico', 'Freios ABS')
   )
   )


for i in range(2):
   for j in range(3):
       print(carros[i][4][j])

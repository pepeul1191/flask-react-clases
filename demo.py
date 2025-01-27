edad = 36
print(edad)
nombre = "pepe"
print(nombre)
peso = 74.3
estatura = 1.70 # estatura en metros
print(peso)
casado = True
print(casado)
edad_esposa = 34
print(edad-edad_esposa)
anio_actual = 2025
anio_mundial = anio_actual + 1
print(anio_mundial)
imc = peso / (estatura * estatura)
print(imc)
imc = peso / (estatura ** 2)
print(imc)
hace_sol = True
hace_calor = True
es_verano = hace_sol and hace_calor
if es_verano == True: 
  print('es verano')
  if anio_actual != anio_mundial:
    print('no se juega el mundial')
  else:
    print('se juega el mundial')
else:
  print('no es verano')
  
mi_lista = [1, 2, 3, "hola", True, None]
print(len(mi_lista))
print(mi_lista[3])
print(mi_lista[len(mi_lista) - 1])

def suma():

import random
import copy 
import numpy as np
import math
import time

def sortSecond(val):
  return val[1] 

def unicos(individuo):
  total_repetidos = 0
  for i in range(len(individuo)):
    repetidos = individuo.count(individuo[i])
    if repetidos>1:
      total_repetidos= total_repetidos +1
  unicos = 9-total_repetidos
  return unicos

def fx_columnas(individuo):
  columnas =  [unicos([individuo[0],individuo[9],individuo[18],individuo[27],individuo[36],individuo[45],individuo[54],individuo[63],individuo[72]]),unicos([individuo[1],individuo[10],individuo[19],individuo[28],individuo[37],individuo[46],individuo[55],individuo[64],individuo[73]]),unicos([individuo[2],individuo[11],individuo[20],individuo[29],individuo[38],individuo[47],individuo[56],individuo[65],individuo[74]]),unicos([individuo[3],individuo[12],individuo[21],individuo[30],individuo[39],individuo[48],individuo[57],individuo[66],individuo[75]]),unicos([individuo[4],individuo[13],individuo[22],individuo[31],individuo[40],individuo[49],individuo[58],individuo[67],individuo[76]]),unicos([individuo[5],individuo[14],individuo[23],individuo[32],individuo[41],individuo[50],individuo[59],individuo[68],individuo[77]]),unicos([individuo[6],individuo[15],individuo[24],individuo[33],individuo[42],individuo[51],individuo[60],individuo[69],individuo[78]]),unicos([individuo[7],individuo[16],individuo[25],individuo[34],individuo[43],individuo[52],individuo[61],individuo[70],individuo[79]]),unicos([individuo[8],individuo[17],individuo[26],individuo[35],individuo[44],individuo[53],individuo[62],individuo[71],individuo[80]])]
  return columnas

def fx_filas(individuo):
  filas = [unicos(individuo[0:9]),unicos(individuo[9:18]),unicos(individuo[18:27]),unicos(individuo[27:36]),unicos(individuo[36:45]),unicos(individuo[45:54]),unicos(individuo[54:63]),unicos(individuo[63:72]),unicos(individuo[72:81])]
  return filas

def fx_cuadritos(individuo):
  cuadritos =  [unicos(individuo[0:3] + individuo[9:12]  + individuo[18:21]),unicos(individuo[3:6] + individuo[12:15] + individuo[21:24]),unicos(individuo[6:9] + individuo[15:18] + individuo[24:27]),unicos(individuo[27:30] + individuo[36:39] +  individuo[45:48]),unicos(individuo[30:33] + individuo[39:42] +  individuo[48:51]),unicos(individuo[33:36] + individuo[42:45] +  individuo[51:54]),unicos(individuo[54:57] + individuo[63:66] +  individuo[72:75]),unicos(individuo[57:60] + individuo[66:69] +  individuo[75:78]),unicos(individuo[60:63] + individuo[69:72] +  individuo[78:81])]
  return cuadritos

def funcion_fitness(individuo): 
  aptitud =sum(fx_columnas(individuo))+sum(fx_filas(individuo))+sum(fx_cuadritos(individuo))
  return aptitud

def generar_individuo(tamaño_individuo,SOL):
  individuo = copy.deepcopy(SOL)
  for i in range(tamaño_individuo):
    if SOL[i] == 0:
      individuo[i] = random.randint(1,9)
  return individuo

def generar_poblacion(tamaño_poblacion,tamaño_individuo,SOL):
  poblacion = []
  for _ in range(tamaño_poblacion):
    individuo = generar_individuo(tamaño_individuo,SOL)
    aptitud = funcion_fitness(individuo)
    poblacion.append([individuo,aptitud])
  return poblacion

def seleccion_torneo(poblacion,no_participantes,tamaño_poblacion):
  participantes = []
  for i in range(no_participantes):
    participantes.append(poblacion[random.randint(0,(tamaño_poblacion)-1)])
  seleccionado = participantes[0]
  i = 1
  while i<no_participantes:
    if participantes[i][1]>seleccionado[1]:
      seleccionado = participantes[i]
    i = i+1
  return seleccionado[0]

def cruze3puntos(padre1,padre2,tamaño_individuo):
  n = random.randint(0,(tamaño_individuo-1))
  n2 = random.randint(n,(tamaño_individuo-1))
  hijo = padre2[0:n]+padre1[n:n2]+padre2[n2:tamaño_individuo]
  return hijo

def mutacion(hijo):
  for _ in range(10):
    hijo[random.randint(0,(tamaño_individuo-1))] = random.randint(1,9)
  return hijo

def escojer_fila(hijo):
  filas = fx_filas(hijo)
  aux = filas.index(min(filas))
  return aux

def escojer_columna(hijo):
  columnas = fx_columnas(hijo)
  aux = columnas.index(min(columnas))
  return aux

def escojer_cuadrito(hijo):
  cuadritos = fx_cuadritos(hijo)
  aux = cuadritos.index(min(cuadritos))
  return aux

def cambiar_fila(hijo,index,SOL):
  n = random.randint(0,8)
  indice = (index*9)+n
  if SOL[indice] == 0:
    hijo[indice] = random.randint(1,9)
  return hijo

def cambiar_columna(hijo,index,SOL):
  n = random.randint(0,8)
  indice = (n*9)+index
  if SOL[indice] == 0:
    hijo[indice] = random.randint(1,9)
  return hijo

def cambiar_cuadrito(hijo,index,SOL):
  if index ==0 :
    numeros = [0,1,2,9,10,11,18,19,20]
    indice = numeros[random.randint(0,8)]
    if SOL[indice]==0:
      hijo[indice] =random.randint(1,9) 
  elif index ==1 :
    numeros = [3,4,5,12,13,14,21,22,23]
    indice = numeros[random.randint(0,8)]
    if SOL[indice]==0:
      hijo[indice] =random.randint(1,9) 
  elif index ==2 :
    numeros = [6,7,8,15,16,17,24,25,26]
    indice = numeros[random.randint(0,8)]
    if SOL[indice]==0:
      hijo[indice] =random.randint(1,9)  
  elif index ==3 :
    numeros = [27,28,29,36,37,38,45,46,47]
    indice = numeros[random.randint(0,8)]
    if SOL[indice]==0:
      hijo[indice] =random.randint(1,9)  
  elif index ==4 :
    numeros = [30,31,32,39,40,41,48,49,50]
    indice = numeros[random.randint(0,8)]
    if SOL[indice]==0:
      hijo[indice] =random.randint(1,9)  
  elif index ==5 :
    numeros = [33,34,35,42,43,44,51,52,53]
    indice = numeros[random.randint(0,8)]
    if SOL[indice]==0:
      hijo[indice] =random.randint(1,9) 
  elif index ==6 :
    numeros = [54,55,56,63,64,65,72,73,74]
    indice = numeros[random.randint(0,8)]
    if SOL[indice]==0:
      hijo[indice] =random.randint(1,9) 
  elif index ==7 :
    numeros = [57,58,59,66,67,68,75,76,77]
    indice = numeros[random.randint(0,8)]
    if SOL[indice]==0:
      hijo[indice] =random.randint(1,9)  
  elif index ==8 :
    numeros = [60,61,62,69,70,71,78,79,80]
    indice = numeros[random.randint(0,8)]
    if SOL[indice]==0:
      hijo[indice] =random.randint(1,9) 
  return hijo

def mutacion2(hijo,SOL):
    hijo = cambiar_fila(hijo,escojer_fila(hijo),SOL)
    hijo = cambiar_columna(hijo,escojer_columna(hijo),SOL)
    hijo = cambiar_cuadrito(hijo,escojer_cuadrito(hijo),SOL)
    hijo = cambiar_fila(hijo,escojer_fila(hijo),SOL)
    hijo = cambiar_columna(hijo,escojer_columna(hijo),SOL)
    hijo = cambiar_cuadrito(hijo,escojer_cuadrito(hijo),SOL)

    return hijo
def mutacion3(hijo,SOL):
    new = generar_individuo(tamaño_individuo,SOL)
    n = random.randint(0,8)
    if n == 0:
        #cambiar los de cuadro 0
        hijo[0:3] = new[0:3]
        hijo[9:12] = new[9:12]
        hijo[18:21] = new[18:21]
    elif n == 1:
        #cambiar los de cuadro 0
        hijo[3:6]  = new[3:6]
        hijo[12:15] = new[12:15]
        hijo[21:24] = new[21:24]
    elif n == 2:
        #cambiar los de cuadro 0
        hijo[6:9] = new[6:9]  
        hijo[15:18] = new[15:18] 
        hijo[24:27] = new[24:27]
    elif n == 3:
        #cambiar los de cuadro 0
        hijo[27:30] = new[27:30] 
        hijo[36:39] = new[36:39] 
        hijo[45:48] = new[45:48]
    elif n == 4:
        #cambiar los de cuadro 0
        hijo[30:33] = new[30:33] 
        hijo[39:42] = new[39:42] 
        hijo[48:51] = new[48:51]
    elif n == 5:
        #cambiar los de cuadro 0
        hijo[33:36] = new[33:36]
        hijo[42:45] = new[42:45]
        hijo[51:54] = new[51:54]
    elif n == 6:
        #cambiar los de cuadro 0
        hijo[54:57] = new[54:57]
        hijo[63:66] = new[63:66]
        hijo[72:75] = new[72:75]
    elif n == 7:
        hijo[57:60] = new[57:60]
        hijo[66:69] = new[66:69]
        hijo[75:78] = new[75:78]
    elif n == 8:
        #cambiar los de cuadro 0 
        hijo[60:63] = new[57:60]
        hijo[69:72] = new[66:69]
        hijo[78:81] = new[75:78]
    return hijo


def mejorcin(poblacion,tamaño_poblacion):
  mejor = poblacion[0]
  i=1
  while i<tamaño_poblacion:
    if poblacion[i][1]>mejor[1]:
      mejor = poblacion[i]
    i = i+1
  return mejor
def validar_SOL(SOL):
    bandera = True
    columnas = [[SOL[0],SOL[9],SOL[18],SOL[27],SOL[36],SOL[45],SOL[54],SOL[63],SOL[72]],[SOL[1],SOL[10],SOL[19],SOL[28],SOL[37],SOL[46],SOL[55],SOL[64],SOL[73]],[SOL[2],SOL[11],SOL[20],SOL[29],SOL[38],SOL[47],SOL[56],SOL[65],SOL[74]],[SOL[3],SOL[12],SOL[21],SOL[30],SOL[39],SOL[48],SOL[57],SOL[66],SOL[75]],[SOL[4],SOL[13],SOL[22],SOL[31],SOL[40],SOL[49],SOL[58],SOL[67],SOL[76]],[SOL[5],SOL[14],SOL[23],SOL[32],SOL[41],SOL[50],SOL[59],SOL[68],SOL[77]],[SOL[6],SOL[15],SOL[24],SOL[33],SOL[42],SOL[51],SOL[60],SOL[69],SOL[78]],[SOL[7],SOL[16],SOL[25],SOL[34],SOL[43],SOL[52],SOL[61],SOL[70],SOL[79]],[SOL[8],SOL[17],SOL[26],SOL[35],SOL[44],SOL[53],SOL[62],SOL[71],SOL[80]]]
    filas = [SOL[0:9],SOL[9:18],SOL[18:27],SOL[27:36],SOL[36:45],SOL[45:54],SOL[54:63],SOL[63:72],SOL[72:81]]
    cuadritos =  [[SOL[0:3] +    SOL[9:12]  + SOL[18:21]],[SOL[3:6] +    SOL[12:15] + SOL[21:24]],[SOL[6:9] +    SOL[15:18] + SOL[24:27]],[SOL[27:30] + SOL[36:39] +  SOL[45:48]],[SOL[30:33] + SOL[39:42] +  SOL[48:51]],[SOL[33:36] + SOL[42:45] +  SOL[51:54]],[SOL[54:57] + SOL[63:66] +  SOL[72:75]],[SOL[57:60] + SOL[66:69] +  SOL[75:78]],[SOL[60:63] + SOL[69:72] +  SOL[78:81]]]
    for j in range(len(columnas)):
        columna =columnas[j]
        fila = filas[j]
        cuadrito =  cuadritos[j]
        for i in range(len(columna)):
            if columna[i] !=0 and columna.count(columna[i])>1:
                bandera = False
        for i in range(len(fila)):
            if fila[i] !=0 and fila.count(fila[i])>1:
                bandera = False
        for i in range(len(cuadrito)):
            if cuadrito[i] !=0 and cuadrito.count(cuadrito[i])>1:
                bandera = False
    return bandera

def imprimir(aux):
    #print(estado)
    
    print(aux[0:3], " ", aux[3:6], " ", aux[6:9])
    print(aux[9:12], " ", aux[12:15], " ", aux[15:18])
    print(aux[18:21], " ", aux[21:24], " ", aux[24:27])
    print(" ")
    print(aux[27:30], " ", aux[30:33], " ", aux[33:36])
    print(aux[36:39], " ", aux[39:42], " ", aux[42:45])
    print(aux[45:48], " ", aux[48:51], " ", aux[51:54])
    print(" ")
    print(aux[54:57], " ", aux[57:60], " ", aux[60:63])
    print(aux[63:66], " ", aux[66:69], " ", aux[69:72])
    print(aux[72:75], " ", aux[75:78], " ", aux[78:81])

"""SOL=[8,0,0,0,0,0,0,0,0,
                0,0,3,6,0,0,0,0,0,
                0,7,0,0,9,0,2,0,0,
                0,5,0,0,0,7,0,0,0,
                0,0,0,0,4,5,7,0,0,
                0,0,0,1,0,0,0,3,0,
                0,0,1,0,0,0,0,6,8,
                0,0,8,5,0,0,0,1,0,
                0,9,0,0,0,0,4,0,0]"""  
#dificil
SOL=[8,0,0,0,0,0,0,0,0,
    0,0,3,6,0,0,0,0,0,
    0,7,0,0,9,0,2,0,0,
    0,5,0,0,0,7,0,0,0,
    0,0,0,0,4,5,7,0,0,
    0,0,0,1,0,0,0,3,0,
    0,0,1,0,0,0,0,6,8,
    0,0,8,5,0,0,0,1,0,
    0,9,0,0,0,0,4,0,0]

"""SOL=[5,3,0,0,7,0,0,0,0,
                6,0,0,1,9,5,0,0,0,
                0,9,8,0,0,0,0,6,0,
                8,0,0,0,6,0,0,0,3,
                4,0,0,8,0,3,0,0,1,
                7,0,0,0,2,0,0,0,6,
                0,6,0,0,0,0,2,8,0,
                0,0,0,4,1,9,0,0,5,
                0,0,0,0,8,0,0,7,9]"""

"""SOL= [2,0,9,0,0,0,6,0,0,0,4,0,8,7,0,0,1,2,8,0,0,0,1,9,0,4,0,
                 0,3,0,7,0,0,8,0,1, 0,6,5,0,0,8,0,3,0, 1,0,0,0,3,0,0,0,7,
                 0,0,0,6,5,0,7,0,9,6,0,4,0,0,0,0,2,0, 0,8,0,3,0,1,4,5,0]"""
#medio
"""SOL=[0,0,0,3,8,0,0,5,0,
                0,0,2,7,0,6,0,0,0,
                0,9,6,5,0,2,0,4,0,
                0,6,0,0,3,7,0,9,8,
                7,0,0,9,0,8,0,0,4,
                9,3,0,2,5,0,0,6,0,
                0,1,0,8,0,3,4,2,0,
                0,0,0,4,0,5,8,0,0,
                0,8,0,0,9,1,0,0,0]"""
#facil
"""SOL=[5,1,7,6,0,0,0,3,4,
               2,8,9,0,0,4,0,0,0,
               3,4,6,2,0,5,0,9,0,
               6,0,2,0,0,0,0,1,0,
               0,3,8,0,0,6,0,4,7,
               0,0,0,0,0,0,0,0,0,
               0,9,0,0,0,0,0,7,8,
               7,0,3,4,0,0,5,6,0,
               0,0,0,0,0,0,0,0,0]"""

"""vacio=[0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0]"""


"""SOL =  [0, 6, 0, 1, 0, 4, 0, 5, 0,
        0, 0, 8, 3, 0, 5, 6, 0, 0,
        2, 0, 0, 0, 0, 0, 0, 0, 1,
        8, 0, 0, 4, 0, 7, 0, 0, 6,
        0, 0, 6, 0, 0, 0, 3, 0, 0,
        7, 0, 0, 9, 0, 1, 0, 0, 4,
        5, 0, 0, 0, 0, 0, 0, 0, 2,
        0, 0, 7, 2, 0, 6, 9, 0, 0,
        0, 4, 0, 5, 0, 8, 0, 7, 0]"""


if validar_SOL(SOL) == False:
  print("coloque una configuracion inicial correcta")
else:
  inicio_de_tiempo = time.time()
  tamaño_poblacion = 100
  tamaño_individuo = 81
  no_participantes = 100
  bandera = True
  #0.4
  probabilidad_mutacion =0.08
  probabilidad_mutacion2 =0.20
  probbilidad_cruce = 1
  boost = 0

  poblacion = generar_poblacion(tamaño_poblacion,tamaño_individuo,SOL)
  iteracion = 0

  while bandera == True:
    nueva_Generacion = []
    for _ in range(int(tamaño_poblacion/2)):
      #seleccion padre 1
      padre1 = seleccion_torneo(poblacion,no_participantes,tamaño_poblacion)
      #seleccion padre 2
      padre2 = seleccion_torneo(poblacion,no_participantes,tamaño_poblacion)
      if random.random() < probbilidad_cruce:
        #hijo1
        hijo1 = cruze3puntos(padre1,padre2,tamaño_individuo)
        #hijo2
        hijo2 = cruze3puntos(padre1,padre2,tamaño_individuo)
      else:
        hijo1 = padre1
        hijo2 = padre2
      if random.random() < probabilidad_mutacion2:
        hijo1 =  mutacion3(hijo1,SOL)
        hijo2 =  mutacion3(hijo2,SOL)
      else:
        #random.random() < probabilidad_mutacion:
        hijo1 =  mutacion2(hijo1,SOL)
        hijo2 =  mutacion2(hijo2,SOL)

      aptitud_hijo1 = funcion_fitness(hijo1)
      aptitud_hijo2 = funcion_fitness(hijo2)
      nueva_Generacion.append([hijo1,aptitud_hijo1])
      nueva_Generacion.append([hijo2,aptitud_hijo2])

    poblacion = nueva_Generacion

    mejor = mejorcin(poblacion,tamaño_poblacion)

    print(iteracion,mejor[1],boost)
    if mejor[1] == 243:
        tiempo_final = time.time() 
        tiempo_transcurrido = tiempo_final - inicio_de_tiempo
        print("\nTomó %d segundos." % (tiempo_transcurrido))
        print("convergio")
        print("iteracion "+str(iteracion))
        print("mejor: ")
        resul=mejor[0]
        #print(mejor[0])
        imprimir(resul)
        print("aptitud del mejor: "+str(mejor[1]))
        bandera = False
    iteracion = iteracion+1
    #if iteracion == 5000:
      #print("probablemente este sudoku no tiene solucion")
      #bandera = False
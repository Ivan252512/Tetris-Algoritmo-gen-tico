import numpy as np
import random
import multiprocessing
import play

"""Algoritmo genético"""

"""Genera cadenas binarias de n bits"""

def generaIndividuo(bits):
    cadena=""
    for i in range(bits):
        cadena+=str(random.randint(0, 1))
    return cadena

"""Convierte valores binarios a decimales con punto decimal, en el intervalo
   [a,b]"""

def binToDec(bin,a,b):
    n=len(bin)
    dec=0
    for i in bin:
        if i=='1':
            dec+=2**(n-1)
        n-=1
    return  a+((dec)/(2**len(bin)-1))*(b-a)

"""Función de reproducción, cruza los "genes" de dos individuos, se utiliza
   cruce uniforme"""

def cruza(bin1,bin2):
    if(len(bin1)==len(bin2)):
        hijo=""
        for i in range(len(bin1)):
            rand=random.randint(0,1)
            if (rand==0):
                hijo+=bin1[i]
            else:
                hijo+=bin2[i]
        return hijo
    else:
        return ("Los binarios deben tener la misma longitud difieren en " +
                 str(abs(len(bin1)-len(bin2))) + " dígitos.")

"""Función de mutación, cambia aleatoriamente el valor de un gen"""

def mutacion(bin):
    bin = list(bin)
    for i in range(int(len(bin)/random.randint(1,5))):
        rand=random.randint(0,len(bin)-1)
        if(bin[rand]=="0"):
            bin[rand]="1"
        if(bin[rand]=="1"):
            bin[rand]="0"
    return "".join(bin)

"""Crea una población de individuos"""
def poblacion(cantidad,bitsDeCadaIndividuo):
    pob=[]
    for i in range(cantidad):
        pob.append(generaIndividuo(bitsDeCadaIndividuo))
    return pob


"""Algoritmo de selección de mínimos, recibe una función de evaluación y una
   lista con individuos(cadenas de binarios) a evaluar, selecciona al 50% más
   apto, los reproduce y la descendencia remplaza al 50% menos apto"""

def eval(x):
   return [play.run_backend_with_parameters(x[0],x[1],x[2],x[3]), x[4], x[5]]

resultado = []
evaluaciones = []
def evolucion(posint,rotint,individu
ospos,individuosrot,iteraciones, board, block):
    global evaluaciones, resultado
    if len(individuospos)!=len(individuosrot):
        return "Las poblaciones iniciales deben tener la misma longitud."
    #Selección

    aEvaluar = []
    evaluacionRepetida = []

    for i in range(len(individuospos)):
        contiene = False
        for j in resultado:
            if (j[1]==individuospos[i] and j[2]==individuosrot[i]):
                evaluacionRepetida.append([j[0], j[1], j[2]])
                contiene = True
                break

        if not contiene:
            aEvaluar.append([board,
                             block,
                             binToDec(individuospos[i],posint[0],posint[1]),
                             binToDec(individuosrot[i],rotint[0],rotint[1]),
                             individuospos[i],
                             individuosrot[i]])

    p = multiprocessing.Pool(4)
    evaluacionNoRepetida = p.map(eval, aEvaluar)

    evaluacion = evaluacionRepetida + evaluacionNoRepetida

    evaluacion.sort()

    for i in evaluacion:
        resultado.append(i)

    mejores50=evaluacion[:int(0.5*len(evaluacion))]
    #Reproducción
    hijos=[]
    mejores50bin=[]


    for i in range(len(mejores50)):
        mejores50bin.append([mejores50[i][4],mejores50[i][5]])
        hijos.append([cruza(mejores50[random.randint(0,int(len(mejores50)/4)-1)][4],
                            mejores50[random.randint(0,int(len(mejores50)/4)-1)][4]),
                      cruza(mejores50[random.randint(0,int(len(mejores50)/4)-1)][5],
                            mejores50[random.randint(0,int(len(mejores50)/4)-1)][5])])

    #Mutación, solo los hijos mutan.
    for i in range(int(len(hijos)/random.randint(1,4))):
        randpos=random.randint(0,len(hijos)-1)
        hijos[randpos][0]=mutacion(hijos[randpos][0])

        randrot=random.randint(0,len(hijos)-1)
        hijos[randrot][1]=mutacion(hijos[randrot][1])


    #Junta a los padres y a los hijos
    nuevaGeneracion=(mejores50bin[:len(mejores50bin)/2]+
                     mejores50bin[:len(mejores50bin)-len(mejores50bin)/2]+
                     hijos)

    genpos=[]
    genrot=[]
    for i in range(len(nuevaGeneracion)):
        genpos.append(nuevaGeneracion[i][4])
        genrot.append(nuevaGeneracion[i][5])


    if(iteraciones==0):
        resultado.sort()
        decimales=[]
        for i in resultado:
            decimales.append([i[0],binToDec(i[1],posint[0],posint[1]),binToDec(i[2],rotint[0],rotint[1])])
        return decimales
    else:
        return  evolucion(posint,rotint,genpos,genrot,iteraciones-1,board,block)

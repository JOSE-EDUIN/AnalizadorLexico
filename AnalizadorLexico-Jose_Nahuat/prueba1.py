import random
 
def concatenarLista(lista_a, lista_b):
    lista_nueva=[]
 
    for i in range(0,len(lista_a)):
        lista_nueva.append(lista_a[i])
 
    for i in range(0,len(lista_b)):
        lista_nueva.append(lista_b[i])
 
    return lista_nueva
 
def imprimirLista(lista, nombre):
    for i in range(0,len(lista)):
        print nombre + "[" + str(i) + "]=" + str(lista[i])
 
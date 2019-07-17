import grafo
import random
import biblioteca
import copy
import collections
SEPARACION_FLECHA = " -> "
SEPARACION_COMA = ", "

def enlistar_recorrido(lista , destino , padres):
    if destino == None:
        return
    enlistar_recorrido(lista, padres[destino],padres)
    lista.append(destino)

def minimo_seguimiento( grafo, origen , destino ):
    """imprime el minimo seguimiento desde origen, hasta destino, de no poder realizarse imprime 'Seguimiento imposible'"""
    #print("minimo_seguimiento")
    padres, ordenes = biblioteca.minimos_seguimientos_hasta_destino( grafo, origen , destino )
    if destino in padres :
        lista = []
        enlistar_recorrido(lista,destino, padres)
        biblioteca.imprimir_lista(lista, SEPARACION_FLECHA)
    else :
        print("Seguimiento imposible")

def k_mas_importantes(grafo,k):
    """devuelve una lista con los k elementos mas importantes del grafo(delincuentes)"""
    centralidad = biblioteca.random_walk(grafo)
    lista_ordenada = biblioteca.counting_sort(centralidad)
    lista_aux = collections.deque()
    #lista = {"v": 2,"v": 1,"s": 5,"a": 2,"d": 9,"e": 9,"c": 4,"a":1 }
    #print("sto es con counting",biblioteca.counting_sort(lista))
    largo_lista =len(lista_ordenada)
    for j in range(largo_lista-1,largo_lista-k,-1):
        lista_aux.append(lista_ordenada[j])
    return lista_aux

def mas_importantes(grafo, cant ):
    """ Imprime, de mayor a menor importancia, los cant delincuentes más importantes."""
    #print("mas_importantes")
    #Betweeness Centrality, aproximado.   o    PageRank.  se usa cualquiera dentro de este
    lista_importantes = k_mas_importantes( grafo, int(cant) )
    biblioteca.imprimir_lista(lista_importantes,SEPARACION_COMA)

def persecucion_rapida(grafo ,parametros, k ):
    """Dado cada uno de los delincuentes pasados (agentes encubiertos),
    obtener cuál es el camino más corto para llegar desde alguno de los delincuentes pasados por parámetro,
    a alguno de los K delincuentes más importantes.
    En caso de tener caminos de igual largo, priorizar los que vayan a un delincuente más importante."""
    print("VER SI ESTO TARDA")
    """"lista_importantes = k_mas_importantes( grafo, int(k) )
    #print(lista_importantes)
    destino = None
    padresresultado = None

    for infiltrado in parametros:
        padres,distancias = biblioteca.minimos_seguimientos_hasta_destino( grafo , infiltrado , None )
        vertice = None
        for importante in lista_importantes:
            if importante == infiltrado:continue
            if destino != None:
                if( distancia_mejor < distancias[importante]) :
                    if ((distancia_mejor  == distancias[importante]) and (lista_importantes.index(importante)> lista_importantes.index(destino))):
                        continue
                    continue
            distancia_mejor = distancias[importante]
            destino = importante
            padresresultado = padres

    lista_a_imprimir=[]
    enlistar_recorrido(lista_a_imprimir, destino , padresresultado)
    biblioteca.imprimir_lista(lista_a_imprimir, SEPARACION_COMA)"""

def filtrar_comunidades( label , integrantes ):
    aux_comunidades = {}

    for j in label:
        if label[j] in integrantes:
            integrantes[ label[j ] ] +=1
        else:
            integrantes[ label[j] ] =1
            aux_comunidades[  label[ j ] ] = []
        aux_comunidades[  label[ j ] ].append(j)
    return aux_comunidades

def imprimir_comunidades(comunidades,  volumen_comunidades, tamanio_minimo):
    contador = 1
    for j in volumen_comunidades.items():
        if volumen_comunidades[ j[0 ] ] >= tamanio_minimo:
            print("comunidad {}: {}".format(contador,SEPARACION_COMA.join(comunidades[j[0]])))
            contador += 1

def mostrar_comunidades( grafo , n):
    """ imprime en pantalla las comunidades de minimo n elementos en ellos"""
    #print("comunidades")
    volumen_comunidad ={}
    comunidades  = filtrar_comunidades( biblioteca.label_propagation( grafo ) , volumen_comunidad )
    imprimir_comunidades( comunidades , volumen_comunidad , int(n))

def divulgar_rumor(grafo ,delicuente ,saltos):
    lista_vertice = biblioteca.radio_rumor(grafo ,delicuente ,int(saltos))
    lista_vertice.remove(delicuente)
    biblioteca.imprimir_lista(lista_vertice,SEPARACION_COMA)

def hay_ciclo(grafo, vertice, saltos , recorrido, contador , origen, apariciones):
    if (contador==saltos):
        if origen == vertice:
            recorrido.append(vertice)
            return True
        else:
            return False

    if apariciones.get(vertice)!=None:

        return False

    recorrido.append(vertice)
    apariciones[vertice]=1
    for j in grafo.adyacentes(vertice):
        if hay_ciclo(grafo, j , saltos , recorrido, contador+1, origen,apariciones):
            return True
    eliminado =recorrido.pop()
    apariciones.pop(eliminado)
    return False

def divulgar_ciclo_n(grafo , delincuente, saltos):
    #print("divulgar_ciclo")
    recorrido = collections.deque()
    contador = 0
    apariciones = {}
    if hay_ciclo(grafo, delincuente, int(saltos), recorrido,contador,  delincuente ,apariciones):
        biblioteca.imprimir_lista(recorrido, SEPARACION_FLECHA)
    else:
         print("No se encontro recorrido")

def componentes_fuert_conex(grafo):
    #print("componentes_fuert_conex")
    conjuntos = biblioteca.cfc(grafo)
    contador = 1
    for c in conjuntos:
        print("CFC {}: {}".format(contador,SEPARACION_COMA.join(c)))
        contador +=1

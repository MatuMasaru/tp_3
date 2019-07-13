import grafo
import random
import biblioteca
import copy

SEPARACION_FLECHA = " -> "
SEPARACION_COMA = ", "

def enlistar_recorrido(lista , destino , padres):
    if destino == None:
        return
    enlistar_recorrido(lista, padres[destino],padres)
    lista.append(destino)
    

def minimo_seguimiento( grafo, origen , destino ):
    """imprime el minimo seguimiento desde origen, hasta destino, de no poder realizarse imprime 'Seguimiento imposible'"""
    padres, vertice = biblioteca.minimos_seguimientos_hasta_destino( grafo, origen , destino )
    print("diccionario de padres ",padres)
    if destino in vertice :
        lista = []
        enlistar_recorrido(lista,destino, padres)
        print("imprimir la lista enlistada")
        biblioteca.imprimir_lista(lista, SEPARACION_FLECHA)
    else :
        print("Seguimiento imposible")

def k_mas_importantes(grafo,k):
    """devuelve una lista con los k elementos mas importantes del grafo(delincuentes)"""
    centralidad = biblioteca.betweeness_centrality(grafo)
    lista = list(sorted(centralidad.items(), key = lambda x:x[1], reverse = True))
    lista_aux = []
    for j in range(k):
       lista_aux.append(lista[j][0])

    return lista_aux

def mas_importantes(grafo, cant ):
    """ Imprime, de mayor a menor importancia, los cant delincuentes más importantes."""
    #Betweeness Centrality, aproximado.   o    PageRank.  se usa cualquiera dentro de este
    lista_importantes = k_mas_importantes( grafo, cant )
    biblioteca.imprimir_lista(lista_importantes,SEPARACION_COMA)

def persecucion_rapida(grafo ,parametros, k ):
    """Dado cada uno de los delincuentes pasados (agentes encubiertos), 
    obtener cuál es el camino más corto para llegar desde alguno de los delincuentes pasados por parámetro, 
    a alguno de los K delincuentes más importantes.
    En caso de tener caminos de igual largo, priorizar los que vayan a un delincuente más importante."""
    lista_importantes = k_mas_importantes( grafo, k )
    delincuentes = parametros.split(',')

    recorridos_delincuentes ={}
    vertice_max = ()
    for i in delincuentes:
        padres,distancias = biblioteca.minimos_seguimientos_hasta_destino( grafo , i , lista_importantes )
        vertice = None
        for j in lista_importantes:
            if j in distancias:
                vertice = j
                break


        if not vertice_max and vertice:
            recorridos_delincuentes = copy.copy(padres)
            vertice_max = ( vertice , distancias[vertice] )

        elif vertice :
            if (vertice_max[1] > distancias[vertice]):
                recorridos_delincuentes = copy.copy(padres)
                vertice_max = ( vertice , distancias[vertice] )

            elif (vertice_max[1] == distancias[vertice])and (lista_importantes.index(vertice_max[0])>lista_importantes.index(vertice_max[0])):
                recorridos_delincuentes = copy.copy(padres)
                vertice_max = ( vertice , distancias[vertice] )
    
    lista_a_imprimir={}
    enlistar_recorrido(lista_a_imprimir, vertice_max[0] , recorridos_delincuentes)
    biblioteca.imprimir_lista(lista_a_imprimir, SEPARACION_FLECHA)


def filtrar_comunidades( label , integrantes ):
    aux_comunidades = {}
    for j in label:
        if label[j] in integrantes:
            integrantes[ label[j ] ] +=1
        else:
            integrantes[ label[j] ] =1
        aux_comunidades[  label[ j] ].append(j)
    return aux_comunidades
        
def imprimir_comunidades(comunidades,  volumen_comunidades, tamanio_minimo):
    contador = 1
    for j in volumen_comunidades:
        if volumen_comunidades[j] >= tamanio_minimo:
            print("comunidad {}: {}".format(contador,comunidades[j].join(SEPARACION_COMA)))
            contador += 1

def mostrar_comunidades( grafo , n):
    """ imprime en pantalla las comunidades de minimo n elementos en ellos"""
    volumen_comunidad ={}
    comunidades  = filtrar_comunidades( biblioteca.label_propagation( grafo ) , volumen_comunidad )
    imprimir_comunidades( comunidades , volumen_comunidad , n)

def divulgar_rumor(grafo ,delicuente ,saltos):
    visitados = []
    contador = 0
    biblioteca.radio_rumor(grafo ,delicuente ,int(saltos) ,contador ,visitados) 
    biblioteca.imprimir_lista(visitados ,SEPARACION_COMA)

def hay_ciclo(grafo, vertice, saltos , recorrido, contador , origen):
    if contador == saltos:
        if origen == vertice:
            recorrido.append(vertice)
            return True
        else:
            return False
    for j in grafo.adyacentes(vertice):
        recorrido.append(vertice)
        if hay_ciclo(grafo, j , saltos , recorrido, contador+1, origen):
            return True
        recorrido.pop()
    return False

def divulgar_ciclo_n(grafo , delincuente, saltos):
    recorrido= []
    contador = 0 
    if hay_ciclo(grafo, delincuente, saltos, recorrido , contador ,delincuente):
        biblioteca.imprimir_lista(recorrido, SEPARACION_FLECHA)
    else:
         print("No se encontro recorrido")   


def componentes_fuert_conex(grafo):
    conjuntos = biblioteca.cfc(grafo)
    contador = 1
    for c in conjuntos:
        print("CFC " + str(contador) + ":",end = '')
        biblioteca.imprimir_lista(c ,SEPARACION_COMA)




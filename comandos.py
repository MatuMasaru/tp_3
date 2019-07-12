import grafo
import random
import biblioteca
import queue

SEPARACION_FLECHA = " -> "
SEPARACION_COMA = ", "

def enlistar_recorrido(lista , destino , padres):
    if destino ==null:
        return
    enlistar_recorrido(lista, padres[destino],padres)
    lista.append(destino)

def minimo_seguimiento( grafo, origen , destino ):
    """imprime el minimo seguimiento desde origen, hasta destino, de no poder realizarse imprime 'Seguimiento imposible'"""
    padres = minimos_seguimientos_hasta_destino( grafo, origen , destino )
    if destino in padres:
        lista = []
        enlistar_recorrido(lista,destino, padres)
        biblioteca.imprimir_lista(lista, SEPARACION_FLECHA)
    else :
        print("Seguimiento imposible")

def mas_importantes(grafo, cant ):
    """ Imprime, de mayor a menor importancia, los cant delincuentes más importantes."""
    #Betweeness Centrality, aproximado.   o    PageRank.  se usa cualquiera dentro de este
    centralidad = biblioteca.betweeness_centrality(grafo)
    lista = list(sorted(centralidad.items(), key = lambda x:x[1], reverse = True))
    biblioteca.imprimir_lista(lista[0:cant],SEPARACION_COMA)

def persecucion_rapida(grafo ,parametros, k ):
    """Dado cada uno de los delincuentes pasados (agentes encubiertos), 
    obtener cuál es el camino más corto para llegar desde alguno de los delincuentes pasados por parámetro, 
    a alguno de los K delincuentes más importantes.
    En caso de tener caminos de igual largo, priorizar los que vayan a un delincuente más importante."""

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
    contador =1
    for j in volumen_comunidades:
        if volumen_comunidades[j] >= tamanio_minimo:
            auxiliar = comunidades[j].join(', ')
            print("comunidad {}: {}".format(contador,auxiliar))
            contador += 1

def mostrar_comunidades( grafo , n):
    """ imprime en pantalla las comunidades de minimo n elementos en ellos"""
    volumen_comunidad ={}
    comunidades  = filtrar_comunidades( biblioteca.label_propagation( grafo ) , volumen_comunidad )
    imprimir_comunidades( comunidades , volumen_comunidad , n)

def divulgar_rumor(grafo, delincuente, saltos):

def divulgar_ciclo_n(grafo , delincuente, saltos):

def componentes_fuert_conex(grafo):
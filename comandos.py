import grafo
import biblioteca
import queue
SEPARACION_FLECHA= " -> "


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


def persecucion_rapida(grafo ,parametros, k ):
    """Dado cada uno de los delincuentes pasados (agentes encubiertos), 
    obtener cuál es el camino más corto para llegar desde alguno de los delincuentes pasados por parámetro, 
    a alguno de los K delincuentes más importantes.
    En caso de tener caminos de igual largo, priorizar los que vayan a un delincuente más importante."""

def encontrar_comunidades(grafo,n):


def divulgar_rumor(grafo, delincuente, saltos):

def divulgar_ciclo_n(grafo,delincuente, saltos):

def componentes_fuert_conex(grafo):
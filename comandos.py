import grafo

def imprimir_pila(pila):
    while not pila_esta_vacia(pila):
        aux = pila.pop()
        print(aux)
        if not pila_esta_vacia(pila):
            print("->")

"""yimi esto esta muy rusticamente realizado, seudocodigo"""
def minimos_seguimientos( grafo, origen , destino ):
    """nos imprime una lista con los delincuentes (su código identificador)
    con los cuáles vamos del delincuente origen al delincuente destino de la forma más rápida.
    En caso de no poder hacer el seguimiento (i.e. no existe camino), imprimir Seguimiento imposible."""
    
    padres={}
    visitados=set()
    q= cola()

    visitados(origen)
    q.encolar(origen)
    padres[origen] = None
    lista=[]
    while not q.esta_vacia(): 
        v = q.desencolar()
        
        for w in grafo.adyacentes( v ):
            if w not in visitados:
                visitados(w)
                padres[w] = v   #esto busca por bfs al destino y si encuentra corta y lo pone como visitado.
                if w == destino :
                    break
                q.encolar(w)

    pila = pila_crear()
    if destino in visitados :   #si esta en visitados, apilo en una pilapor el ordene me fijo el padre, 
        pila.apilar(destino)
        aux = destino
        while not aux :
            aux= padres[aux]
            pila.apilar(aux)
        imprimir_pila(pila)
         
    else :
        print("seguimiento imposible")

    
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
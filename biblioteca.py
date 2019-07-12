import grafo
import collections


def imprimir_lista(lista, separador):

    print(lista.join(separador))

def camino_minimo_bfs(grafo, origen):
    """devuelve dos diccionarios uno de ordenes y otro de dependencias(padres) """
    visitados = set()
    padres = {}
    orden = {}
    cola = collections.deque()

    visitados.add(origen)
    padres[origen] = None
    orden[origen] = 0
    cola.append(origen)

    while cola:
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                padres[w] = v
                orden[w] = orden[v] + 1
                cola.append(w)
    
    return orden,padres

def minimos_seguimientos_hasta_destino( grafo, origen , destino ):
    """ devuelve un diccionario de padres, de dependencias de como llegar desde origen a destino, en caso que no llega a destino
        devuelve el diccionario pero 'destino' no estara en el diccionario"""
    
    padres={}
    visitados=set()
    
    cola = collections.deque()

    visitados.add(origen)
    cola.append(origen)

    padres[origen] = None

    while cola: 
        v = cola.popleft()
        
        for w in grafo.adyacentes( v ):
            if w not in visitados:
                visitados.add(w)
                padres[w] = v   #esto busca por bfs al destino y si encuentra corta y lo pone como visitado.
                if w == destino :
                    break
                cola.append(w)

def ordenar_vertices(grafo , distancia):# aplicar counting sort. para la centralidad.
    """devuelve un iterable  ordenado de mayor a menor  en funcion del valor del dict distancia"""
    return list(sorted(distancia.items(),key = lambda x:x[1] , reverse = True ))

def betweeness_centrality(grafo):
    cent = {}
    for v in grafo: cent[v] = 0
    for v in grafo:
        # hacia todos los demas vertices
        distancia, padre = camino_minimo_bfs(grafo, v)          #aplicar camino minimo

        cent_aux = {}
        for w in grafo: cent_aux[w] = 0
        # Aca filtramos (de ser necesario) los vertices a distancia infinita, 
        # y ordenamos de mayor a menor
        vertices_ordenados = ordenar_vertices(grafo, distancia) 

        for w in vertices_ordenados:
            cent_aux[padre[w]] += 1 + cent_aux[w]
        # le sumamos 1 a la centralidad de todos los vertices que se encuentren en 
        # el medio del camino
        for w in grafo:
            if w == v: continue
            cent[w] += cent_aux[w]
    return cent

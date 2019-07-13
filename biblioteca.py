import grafo
import random
import collections

LABEL_ITERACIONES = 100

def imprimir_lista(lista, separador):

    print(separador.join(lista))

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

    return orden ,padres

def minimos_seguimientos_hasta_destino(grafo, origen ,destino):
    """ devuelve un diccionario de padres, de dependencias de como llegar desde origen a destino, en caso que no llega a destino
        devuelve el diccionario pero 'destino' no estara en el diccionario"""
    padres={}
    visitados=set()
    orden = {}
    cola = collections.deque()

    visitados.add(origen)

    orden[origen] = 0
    padres[origen] = None

    cola.append(origen)
    while cola:

        v = cola.popleft()

        for w in grafo.adyacentes( v ):
            if w not in visitados:
                visitados.add(w)
                padres[w] = v   #esto busca por bfs al destino y si encuentra corta y lo pone como visitado.
                orden[w] = orden[v] + 1
                if w in destino:
                    return padres,orden 
                cola.append(w)
    return padres,orden 

def ordenar_vertices(grafo, distancia):# aplicar counting sort. para la centralidad.
    """devuelve un iterable  ordenado de mayor a menor  en funcion del valor del dict distancia"""
    return list(sorted(distancia.items(),key = lambda x:x[1] , reverse = True ))

def betweeness_centrality(grafo):
    cent = {}
    for i in grafo.vertices: cent[i] = 0
    for v in grafo.vertices:
        # hacia todos los demas vertices
        distancia, padre = camino_minimo_bfs(grafo, v)          #aplicar camino minimo

        cent_aux = {}
        for w in grafo.vertices: cent_aux[w] = 0
        # Aca filtramos (de ser necesario) los vertices a distancia infinita, 
        # y ordenamos de mayor a menor
        vertices_ordenados = ordenar_vertices(grafo, distancia) 
       
        for w in vertices_ordenados:
            if padre[w[0]] !=None:
                cent_aux[padre[w[0]]] += 1 + cent_aux[w[0]]
        # le sumamos 1 a la centralidad de todos los vertices que se encuentren en 
        # el medio del camino
       
        for w in grafo.vertices:
            if w == v: continue
            cent[w] += cent_aux[w]

    return cent

def max_freq(adyacentes, label):
    dict_recurrencia = {}
    for j in adyacentes:
        if j not in dict_recurrencia:
            dict_recurrencia[ label [j] ] = 1
        else :
            dict_recurrencia[ label [j] ] += 1
    maximo = max(dict_recurrencia.items(), key = lambda x:x[1] )
    return maximo[0]


def label_propagation( grafo ):
    label = {}
    contador = 0
    for v in grafo.vertices:
        label[v]= contador
        contador += 1
    vertices = label.keys()

    for j in range(LABEL_ITERACIONES):
        random.shuffle(vertices)
        for i in vertices:
            label[i] = max_freq(grafo.adyacentes(i), label)
    return label

def radio_rumor(grafo ,delicuente ,saltos ,contador ,visitados):
    visitados.append(delicuente)
    for w in grafo.adyacentes(delicuente):
        if ((w is not visitados) and (contador < saltos)):
            contador += 1
            radio_rumor(grafo ,delicuente ,saltos ,contador ,visitados)
            contador -= 1

def dfs_cfc(grafo, v, visitados, orden, p, s, cfcs, en_cfs):
    visitados.agregar(v)
    s.deque(v)
    p.deque(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            orden[w] = orden[v] + 1
            dfs_cfc(grafo, w, visitados, orden, p, s, cfcs, en_cfs)
        elif w not in en_cfs:
            while orden[p(-1)] > orden[w]:
                p.pop()

    if p(-1) == v:
        p.pop()
        z = None
        nueva_cfc = []
    while z != v:
        z = s.desapilar()
        en_cfs.agregar(z)
        nueva_cfc.append(z)
        cfcs.append(nueva_cfc)

def cfc(grafo):
    visitados = set()
    orden = {}
    pila_p = collections.deque()
    pila_s = collections.deque()
    cfcs = []
    en_cfs = set()
    for v in grafo:
        if v not in visitados:
            orden[v] = 0
            dfs_cfc(grafo, v, visitados, orden, pila_p, pila_s, cfcs, en_cfs)
    return cfcs

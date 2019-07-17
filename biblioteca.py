import grafo
from operator import itemgetter
import random
import collections

LARGO_RECORRIDO = 1000
LABEL_ITERACIONES= 500
def imprimir_lista(lista, separador):
    print(separador.join(lista))


def minimos_seguimientos_hasta_destino(grafo, origen ,destino = None):
    """ devuelve un diccionario de padres, de dependencias de como llegar desde origen a destino, en caso que no llega a destino
        devuelve el diccionario pero 'destino' no estara en el diccionario"""
    padres={}
    visitados=set()
    cola = collections.deque()
    orden= {}
    visitados.add(origen)
    padres[origen] = None
    orden [origen] = 0
    cola.append(origen)
    while cola:
        vertice = cola.popleft()
        for adyacente in grafo.adyacentes(vertice):
            if not adyacente in visitados:
                visitados.add(adyacente)
                padres[adyacente] = vertice  #esto busca por bfs al destino y si encuentra corta y lo pone como visitado.
                orden[adyacente] =orden[vertice] + 1
                if destino and adyacente == destino:
                    return padres,orden

                cola.append(adyacente)
    return padres, orden

def ordenar_vertices(grafo , distancia):# aplicar counting sort. para la centralidad.
    """devuelve un iterable  ordenado de mayor a menor  en funcion del valor del dict distancia"""
    return sorted(distancia.items(), key=itemgetter(1), reverse = True)


def counting_sort(centralidad, minimos = True):
    lista_valores = list(centralidad.values())
    minimo = min(lista_valores)
    maximo =max(lista_valores)
    rango = (maximo-minimo)+1
    frecuencias = []
    # inicializo todas las frecuencias en 0
    for _ in range(rango):
        frecuencias.append(0)
    # cuento la frecuencia de cada numero
    for valor in lista_valores:
        frecuencias[valor-minimo] += 1
    # obtengo el arreglo de sumas acumuladas
    # pongo la primera posicion en 0
    acum = []
    for i in range (rango+1):acum.append(0)
    for i in range(rango):
        acum[i+1] = acum[i] +frecuencias[i]

    # pongo los valores en orden donde corresponde
    ordenadas = []
    for i in range(len(lista_valores)):
        ordenadas.append(None)

    for vertice in centralidad.keys():
        indice = None
        if minimos :
            indice = acum[centralidad[vertice]-minimo]
        else:
            indice = len(ordenadas)-acum[centralidad[vertice]-minimo]-1
        ordenadas[indice] = vertice
        acum[centralidad[vertice] -minimo] += 1
    return ordenadas


def random_walk(grafo):
    importancia_delincuente = {}
    vertices =[]

    for vertice in grafo._vertices():
        vertices.append(vertice)

    for i in range(0, 3000):

        vertice_act = random.choice(vertices)

        for i in range(0, 150):

            if vertice_act in importancia_delincuente:
                importancia_delincuente[vertice_act] += 1
            else:
                importancia_delincuente[vertice_act] = 1

            vertice_act = random.choice(grafo.adyacentes(vertice_act))

    return importancia_delincuente



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
    vertices = list(label.keys())

    for j in range(LABEL_ITERACIONES):
        random.shuffle(vertices)
        for i in vertices:
            label[i] = max_freq(grafo.adyacentes(i), label)
    return label

def radio_rumor(grafo, delicuente ,saltos):
    visitados = set()
    orden = {}
    cola = collections.deque()
    visitados.add(delicuente)
    orden[delicuente] = 0
    cola.append(delicuente)
    while cola:
        v = cola.popleft()
        if (orden[v] == saltos):
                    return visitados
        for adyacente in grafo.adyacentes(v):
            if not adyacente in visitados:
                visitados.add(adyacente)
                orden[adyacente] = orden[v]+1
                cola.append(adyacente)
    return visitados

def dfs_cfc(grafo, v, visitados, orden, p, s, cfcs, en_cfs):
    visitados.add(v)
    s.append(v)
    p.append(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            orden[w] = orden[v] + 1
            dfs_cfc(grafo, w, visitados, orden, p, s, cfcs, en_cfs)
        elif not w in en_cfs:
            while orden[p[-1]] > orden[w]:
                p.pop()

    if p[-1] == v:
        p.pop()
        z = None
        nueva_cfc = []
        while not z == v:
            z = s.pop()
            en_cfs.append(z)
            nueva_cfc.append(z)
        cfcs.append(nueva_cfc)

def cfc(grafo):
    visitados = set()
    orden = {}
    pila_p = []
    pila_s = []
    cfcs = []
    en_cfs = []
    for v in grafo.vertices:
        if v not in visitados:
            orden[v] = 0
            dfs_cfc(grafo, v, visitados, orden, pila_p, pila_s, cfcs, en_cfs)
    return cfcs

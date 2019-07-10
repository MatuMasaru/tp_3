import grafo

def camino_minimo_bfs(grafo, origen):
    """este es el camino minimo para la centralidad, aun no entiendo sobre colas, odio no tener internet"""
    visitados = set()
    padres = {}
    orden = {}
    q = cola()
    for j in grafo()
    visitados(origen)
    padres[origen] = None
    orden[origen] = 0
    q.encolar(origen)

    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados[w]
                padres[w] = v
                orden[w] = orden[v] + 1
                q.encolar(w)
    
    return orden,padres

def ordenar_vertices(grafo , distancia):# aplicar counting sort. para la centralidad.

    """hay que ordenar, nos sirve  usar diccionario.items()
    devuelve una secuencia desordenada con tuplas de dos elementos, 
    en las que el primer elemento es la clave y el segundo el valor"""
    diccionario.items() # y ordenar por countingsort, ordenariamos con un sort pero solo teniendo en cuenta valor.

def centralidad(grafo):
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

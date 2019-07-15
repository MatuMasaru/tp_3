
import
LARGO_RECORRIDO = 1500
prob = [0.05, 0.95]
def random_walk(grafo):

    apariciones = {}
    lista_vertices = grafo.vertices()
    for w in lista_vertices :apariciones[W]= 0
    cantidad_vertices = len(grago)

    for j in range (0, LARGO_RECORRIDO):
        vertice_origen = random.choice(lista_vertices)
        apariciones[vertice_origen] +=1
        contador = 0
        for i in range(0, cantidad_vertices +contador):
            if not grafo.adyacentes(vertice_origen):
                contador = cantidad_vertices -1
                continue
            vertice_origen = choice(list(grafo.adyacentes(vertice_origen)))
            apariciones[vertice_origen] += 1

            if i == (cantidad_vertices + contador -1 ):
                contador = 0
    return apariciones

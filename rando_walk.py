def random_walk(grafo):
    vertices_apariciones = {}
    cant_recorridos= len(grafo)
    largo =len(grafo)
    lista_vertices = grafo._vertices()
    lista_vertice = random.choices(lista_vertices,k =len(grafo))

    for v in grafo._vertices():
        vertices_apariciones[v] = 0
    #print("vertices grafo",grafo._vertices())
    for k in range (0, cant_recorridos):
        vertice_origen = lista_vertice[k]
        vertices_apariciones[vertice_origen] += 1
        iteraciones_extra=0
        for i in range (0, largo ):
            lista_Adyacentes= list(grafo.adyacentes(vertice_origen))
            if not lista_Adyacentes:
                iteraciones_extra = largo - i
                continue
            vertice_origen = random.choice(lista_Adyacentes)
            vertices_apariciones[vertice_origen] += 1
            if i == (largo + iteraciones_extra - 1):
                iteraciones_extra = 0
    return vertices_apariciones

def random_walk(grafo):
    apariciones = {}
    lista_vertices = list(grafo.vertices.keys())
    #print("lista vertices claves",lista_vertices)

    for w in lista_vertices :
        apariciones[w]= 0

    largo_recorrido = 5
    cantidad_de_recorrido = 2000
    print("largo del grafo:", len(grafo))

    for j in range (cantidad_de_recorrido):
        vertice_origen = random.choice(lista_vertices)
        #apariciones[vertice_origen] +=1
        for i in range(largo_recorrido):
            vertice_origen = random.choice(grafo.adyacentes(vertice_origen))
            if vertice_origen not in apariciones:
                apariciones[vertice_origen] = 1
            else:
                apariciones[vertice_origen] += 1
    return apariciones

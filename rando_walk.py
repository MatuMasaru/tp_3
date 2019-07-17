def random_walk(grafo):
    def random_walk(grafo):
        apariciones = {}
        cant_recorridos= len(grafo)*20
        largo =5
        vertices_random = random.choices(grafo._vertices() ,k =len(grafo)*20)

        for v in grafo._vertices():
            vertices_apariciones[v] = 0
        #print("vertices grafo",grafo._vertices())
        for k in range (0, cant_recorridos):
            vertice_origen = vertices_random[k]
            vertices_apariciones[vertice_origen] += 1

            for i in range (0, largo ):
                lista_Adyacentes= list(grafo.adyacentes(vertice_origen))
                if not lista_Adyacentes:
                    iteraciones_extra = largo - i
                    continue
                vertice_origen = random.choice(lista_Adyacentes)
                apariciones[vertice_origen] += 1
        return apariciones

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
    def pagerank_grafo(grafo):
    sinks = 0
    k = 20
    d = 0.85
    n = len(grafo)
    sumat = {}
    grado = {}
    old_pr = {}
    new_pr = {}

    # Calculo grados de salida e inicializo PR
    for vert in grafo:
        grado[vert] = 0
        old_pr[vert] = 1 / n
    for vert in grafo:
        for ady in grafo.adyacentes(vert):
            grado[vert] += 1

    for _ in range(0, k):
        # Calculo sinks
        sinks = 0
        for vert in grafo:
            if grado[vert] == 0: sinks += old_pr[vert]
            sumat[vert] = 0 # Pongo todas las sumatorias en 0

        # Calculo sumatoria de cada vertice
        for vert in grafo:
            for ady in grafo.adyacentes(vert):
                sumat[ady] += (old_pr[vert] / grado[vert])

        # Calculo PR para cada vertice
        for vert in grafo:
            new_pr[vert] = ((1 - d + d * sinks) / n) + (d * sumat[vert])
        old_pr = new_pr
return old_pr

def random_walk(grafo):
    apariciones = {}
    lista_vertices = grafo._vertices()
    #print("lista vertices claves",lista_vertices)

    for w in lista_vertices :
        apariciones[w]= 0
    cantidad_de_recorrido = len(grafo)

    for j in range (0, cantidad_de_recorrido):
        origen = random.choice(lista_vertices)
        apariciones[origen] +=1
        contador = 0
        for i in range(0, cantidad_de_recorrido +contador):
            if not grafo.adyacentes(origen):
                contador = cantidad_de_recorrido -1
                continue
            origen = random.choice(list(grafo.adyacentes(origen)))
            apariciones[origen] += 1

            if i == (cantidad_de_recorrido + contador -1 ):
                contador = 0
    return apariciones

    nlargest(int(cantidad), pr, key=pr.get)

    def counting_sort(centralidad):
        lista_valores = list(centralidad.values())
        minimo = min(lista_valores)
        print(minimo)
        maximo =max(lista_valores)
        rango = (maximo-minimo)+1
        frecuencias = []
    	# inicializo todas las frecuencias en 0
        print(rango)
        for _ in range(rango):
            frecuencias.append(0)
        # cuento la frecuencia de cada numero
        for valor in lista_valores:
            frecuencias[valor-minimo]= frecuencias[valor-minimo]+ 1
        # obtengo el arreglo de sumas acumuladas
        # pongo la primera posicion en 0
        acum = []
        acum.append(0)
        for i in range(1,rango):
            acum.append(acum[i - 1] + frecuencias[i - 1])
        # pongo los valores en orden donde corresponde
        ordenadas = []
        for i in range(len(lista_valores)):
            ordenadas.append(None)
        for vertice in centralidad.keys():
            indice = acum[centralidad[vertice]-minimo]
            ordenadas[indice] = vertice
            acum[centralidad[vertice] -minimo] += 1
        return ordenadas

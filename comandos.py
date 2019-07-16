import grafo
import random
import biblioteca
import copy
import collections

SEPARACION_FLECHA = " -> "
SEPARACION_COMA = ", "

def enlistar_recorrido(lista , destino , padres):
    if destino == None:
        return
    enlistar_recorrido(lista, padres[destino],padres)
    lista.append(destino)

def minimo_seguimiento( grafo, origen , destino ):
    """imprime el minimo seguimiento desde origen, hasta destino, de no poder realizarse imprime 'Seguimiento imposible'"""
    #print("minimo_seguimiento")
    padres, ordenes = biblioteca.minimos_seguimientos_hasta_destino( grafo, origen , destino )
    if destino in padres :
        lista = []
        enlistar_recorrido(lista,destino, padres)
        biblioteca.imprimir_lista(lista, SEPARACION_FLECHA)
    else :
        print("Seguimiento imposible")

def k_mas_importantes(grafo,k):
    """devuelve una lista con los k elementos mas importantes del grafo(delincuentes)"""
    centralidad = biblioteca.random_walk(grafo)
    lista = list(sorted(centralidad.items(), key = lambda x:x[1], reverse = True))
    lista_aux = []
    for j in range( k ):
       lista_aux.append(lista[j][0])
    return lista_aux

def mas_importantes(grafo, cant ):
    """ Imprime, de mayor a menor importancia, los cant delincuentes más importantes."""
    #print("mas_importantes")
    #Betweeness Centrality, aproximado.   o    PageRank.  se usa cualquiera dentro de este
    lista_importantes = k_mas_importantes( grafo, int(cant) )
    biblioteca.imprimir_lista(lista_importantes,SEPARACION_COMA)

def persecucion_rapida(grafo ,parametros, k ):
    """Dado cada uno de los delincuentes pasados (agentes encubiertos),
    obtener cuál es el camino más corto para llegar desde alguno de los delincuentes pasados por parámetro,
    a alguno de los K delincuentes más importantes.
    En caso de tener caminos de igual largo, priorizar los que vayan a un delincuente más importante."""
    #print("persecucion_rapida")
    lista_importantes = k_mas_importantes( grafo, int(k) )
    delincuentes = parametros
    recorridos_delincuentes ={}
    vertice_max = ()
    for i in delincuentes:
        padres,distancias = biblioteca.minimos_seguimientos_hasta_destino( grafo , i , lista_importantes )
        vertice = None
        for j in lista_importantes:
            if j in distancias:
                vertice = j
                break
        if not vertice_max and vertice:
            recorridos_delincuentes = copy.copy(padres)
            vertice_max = ( vertice , distancias[vertice] )
        elif vertice :
            if (vertice_max[1] > distancias[vertice]):
                recorridos_delincuentes = copy.copy(padres)
                vertice_max = ( vertice , distancias[vertice] )
            elif (vertice_max[1] == distancias[vertice])and (lista_importantes.index(vertice_max[0])>lista_importantes.index(vertice_max[0])):
                recorridos_delincuentes = copy.copy(padres)
                vertice_max = ( vertice , distancias[vertice] )

    lista_a_imprimir=[]
    enlistar_recorrido(lista_a_imprimir, vertice_max[0] , recorridos_delincuentes)
    biblioteca.imprimir_lista(lista_a_imprimir, SEPARACION_COMA)

def filtrar_comunidades( label , integrantes ):
    aux_comunidades = {}

    for j in label:
        if label[j] in integrantes:
            integrantes[ label[j ] ] +=1
        else:
            integrantes[ label[j] ] =1
            aux_comunidades[  label[ j ] ] = []
        aux_comunidades[  label[ j ] ].append(j)
    return aux_comunidades

def imprimir_comunidades(comunidades,  volumen_comunidades, tamanio_minimo):
    contador = 1
    for j in volumen_comunidades.items():
        if volumen_comunidades[ j[0 ] ] >= tamanio_minimo:
            print("comunidad {}: {}".format(contador,SEPARACION_COMA.join(comunidades[j[0]])))
            contador += 1

def mostrar_comunidades( grafo , n):
    """ imprime en pantalla las comunidades de minimo n elementos en ellos"""
    #print("comunidades")
    volumen_comunidad ={}
    comunidades  = filtrar_comunidades( biblioteca.label_propagation( grafo ) , volumen_comunidad )
    imprimir_comunidades( comunidades , volumen_comunidad , int(n))

def divulgar_rumor(grafo ,delicuente ,saltos):
    lista_vertice = biblioteca.radio_rumor(grafo ,delicuente ,int(saltos))
    lista_vertice.remove(delicuente)
    biblioteca.imprimir_lista(lista_vertice,SEPARACION_COMA)

def hay_ciclo(grafo, vertice, saltos , recorrido, contador , origen):
    if (contador==saltos):
        if origen == vertice:
            recorrido.append(vertice)
            return True
        else:
            return False

    if vertice in recorrido:
        return False

    recorrido.append(vertice)
    for j in grafo.adyacentes(vertice):
        if hay_ciclo(grafo, j , saltos , recorrido, contador+1, origen):
            return True
    recorrido.pop()
    return False

def divulgar_ciclo_n(grafo , delincuente, saltos):
    #print("divulgar_ciclo")
    recorrido = []
    contador = 0
    if hay_ciclo(grafo, delincuente, int(saltos), recorrido,contador,  delincuente ):
        biblioteca.imprimir_lista(recorrido, SEPARACION_FLECHA)
    else:
         print("No se encontro recorrido")

def componentes_fuert_conex(grafo):
    #print("componentes_fuert_conex")
    conjuntos = biblioteca.cfc(grafo)
    contador = 1
    for c in conjuntos:
        print("CFC {}: {}".format(contador,SEPARACION_COMA.join(c)))
        contador +=1

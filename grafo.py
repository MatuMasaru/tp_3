import random

class Grafo:
    def __init__(self):
        " crea el grafo vacio"
        self.numero_vertices = 0
        self.vertices = {}

    def vertice_pertenece(self, vertice):
        "devuelve true si el vertice pertenece , o false en caso contrario"
        return vertice in self.vertices

    def agregar_vertice(self, nuevo_vertice):
        "agrega un vertice al grafo"
        if not self.vertice_pertenece(nuevo_vertice):
            self.vertices[nuevo_vertice] = {}
            self.numero_vertices += 1
            return True
        return False

    def adyacentes(self, vertice):
        if not self.vertice_pertenece(vertice):
            return None
        return self.vertices[vertice].keys()

    def remover_vertice(self, vertice):
        if vertice in self.vertices:
            for ady in self.vertices[vertice].keys():
                del self.vertices[ady][vertice]
            del self.vertices[vertice]
            self.numero_vertices -=1
            return True
        return False

    def esta_conectado(self, vertice_1, vertice_2):
        if self.vertice_pertenece(vertice_1) and self.vertice_pertenece(vertice_2):#si ambos pertenecen al grafo
            
           # return vertice_1 in self.vertices[vertice_2]    #el mensaje es unidireccional, de vertice_1 a vertice_2
            #        **miralo yimi**                             #solo ipporta en esta direccion si esta conectado
            if vertice_2 in self.adyacentes(vertice_1):
                return True
        return False


    def agregar_arista(self, salida_vertice, entrada_vertice, peso=1):
        if not self.esta_conectado(salida_vertice, entrada_vertice):    #SI NO ESTA CONECTADO, agrego(seria los corchetes) 
            self.vertices[entrada_vertice][salida_vertice] = peso       #y le coloco el peso 
            return True
        return False

    def remover_arista(self, vertice_1, vertice_2): #deberia devolverse la arista
        if not self.esta_conectado(vertice_1, vertice_2): #si no esta no se remueve
            return self.vertices[vertice_1].pop(vertice_2)   #sacar arista y devolverlo 
        return None

    def obtener_vertices(self):
        return self.vertices.keys()

    def __len__(self):
        return self.numero_vertices


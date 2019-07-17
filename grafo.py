import random

class Grafo:
    def __init__(self):
        """ crea el grafo vacio"""
        self.numero_vertices = 0
        self.vertices = {}

    def vertice_pertenece(self, vertice):
        return vertice in self.vertices

    def agregar_vertice(self, nuevo_vertice):
        """agrega un vertice al grafo"""
        if not self.vertice_pertenece(nuevo_vertice):
            self.vertices[nuevo_vertice] = {}
            self.numero_vertices += 1
            return True
        return False

    def adyacentes(self, vertice):
        if not self.vertice_pertenece(vertice):
            return None
        return list(self.vertices[vertice].keys())

    def remover_vertice(self, vertice):
        if vertice in self.vertices:
            for ady in self.vertices[vertice].keys():
                del self.vertices[ady][vertice]
            del self.vertices[vertice]
            self.numero_vertices -=1
            return True
        return False

    def esta_conectado(self, vertice_1, vertice_2):
        if self.vertice_pertenece(vertice_1) and self.vertice_pertenece(vertice_2):
            if vertice_2 in self.adyacentes(vertice_1):
                return True
        return False


    def agregar_arista(self, salida_vertice, entrada_vertice, peso=1):
        if not self.pertenece(entrada_vertice):
			self.agregar_vertice(entrada_vertice)
		if not self.pertenece(salida_vertice):
			self.agregar_vertice(salida_vertice)
        self.vertices[salida_vertice][entrada_vertice] = peso

    def remover_arista(self, vertice_1, vertice_2): #deberia devolverse la arista
        if not self.esta_conectado(vertice_1, vertice_2): #si no esta no se remueve
            self.vertices[vertice_1].pop(vertice_2)   #sacar arista y devolverlo

    def _vertices(self):
        return self.vertices.keys()

    def cantidad_vertice(self):
        return self.numero_vertices

import random

class Grafo:
    def __init__(self):
        self.numero_vertices = 0
        self.vertices = {}

    def vertice_pertenece(self, vertice):
        return vertice in self.vertices

    def agregar_vertice(self, nuevo_vertice):
        if not self.vertice_pertenece(nuevo_vertice):
            self.vertices[nuevo_vertice] = {}

    def adyacentes(self, vertice):
        if not self.vertice_pertenece(vertice):
            return None
        return self.vertices[vertice].keys()

    def remover_vertice(self, vertice):
        if vertice in self.vertices:
            for ady in self.vertices[vertice].keys():
                del self.vertices[ady][vertice]
            del self.vertices[vertice]

    def esta_conectado(self, vertice_1, vertice_2):
        if self.vertice_pertenece(vertice_1) or self.vertice_pertenece(vertice_2):
            return vertice_1 in self.vertices[vertice_2]
        return False


    def agregar_arista(self, salida_vertice, entrada_vertice, peso=2):
        if not self.esta_conectado(salida_vertice, entrada_vertice):
            self.vertices[entrada_vertice][salida_vertice] = -peso
            self.vertices[salida_vertice][entrada_vertice] = peso

    def remover_arista(self, vertice_1, vertice_2):
        if not self.esta_conectado(vertice_1, vertice_2):
            del self.vertices[vertice_1][vertice_2]
            del self.vertices[vertice_2][vertice_1]

    def obtener_vertices(self):
        return self.vertices.keys()

    def __len__(self):
        return self.numero_vertices


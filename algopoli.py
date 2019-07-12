import grafo
import sys
import comandos

MIN_SEGUIMIENTOS = "min_segimientos"
MAS_IMPORTARNTES = "mas_imp"
PERSECUCION = "persecucion"
COMUNIDADES = "comunidades"
DIVULGAR = "divulgar"
DIVULGAR_CICLO = "divulgar_ciclo"
COM_FUERT_CONEXAS = "cfc"

def procesar_linea(separador,linea):
    """devuelve una lista de string separados por el separador(como el split)"""
    return (linea.rstrip('\n')).split(separador)

def cargar_vertices(archivo, grafo):
    for linea in archivo :
        vertices = procesar_linea('\t',linea)
        for i in vertices:
            if not grafo.vertice_pertenece(i):
                grafo.agregar_vertice(i)
        grafo.agregar_arista(vertices[0],vertices[1])

def ejecutar_comando(comando, grafo, parametros):
    if comando is MIN_SEGUIMIENTOS:
        comandos.minimo_seguimiento(grafo,parametros[1],parametros[2])
    elif comando is MAS_IMPORTARNTES:
        comandos.mas_importantes(grafo,int(parametros[1]) )
    elif comando is PERSECUCION:
        comandos.persecucion_rapida(grafo ,(parametros[1]).split(','), parametros[2] )
    elif comando is COMUNIDADES:
        comandos.mostrar_comunidades(grafo,parametros[1])
    elif comando is DIVULGAR:
        comandos.divulgar_rumor(grafo, parametros[1], parametros[2])
    elif comando is DIVULGAR_CICLO:
        comandos.divulgar_ciclo_n(grafo,parametros[1], parametros[2])
    elif comando is COM_FUERT_CONEXAS:      
        comandos.componentes_fuert_conex(grafo)
    
def realizar_comandos(graf):
    archivo = "stdin"
    for linea in archivo:
        linea = procesar_linea(" ", linea)
        ejecutar_comando(linea[0],graf, linea)

def main():
    nom_archivo = sys.argv[1]
            #archivo = open(nom_archivo, 'r')
    graf = grafo.Grafo()  #crea el grafo
    with open(nom_archivo) as archivo:
        """if not archivo:
            print("no se puede abrir") 
             return"""
        cargar_vertices(archivo, graf)
    if graf.__len__:
        realizar_comandos(graf)





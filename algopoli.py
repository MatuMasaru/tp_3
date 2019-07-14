#!/usr/bin/python3
import grafo
import sys
import comandos

MIN_SEGUIMIENTOS = "min_seguimientos"
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
    numero = 0
    if (comando == MIN_SEGUIMIENTOS):
        print("############################################################")
        print("empieza min_segimiento")
        print("############################################################")
        comandos.minimo_seguimiento(grafo,parametros[1],parametros[2])
    elif comando == MAS_IMPORTARNTES:
        if parametros[1].isdigit():
            print("############################################################")
            print("empieza mas_importantes")
            print("############################################################")
            numero = int(parametros[1]) 
            comandos.mas_importantes(grafo,numero )
        else:
            print("el parametro ",parametros[1],"no es un numero")
    elif comando == PERSECUCION:
        if parametros[2].isdigit():
            print("empieza persecucion")
            print("############################################################")
            numero = int(parametros[2])
            comandos.persecucion_rapida(grafo ,(parametros[1]).split(','), numero)
        else:
            print("el parametro ",parametros[2],"no es un numero")
    elif comando == COMUNIDADES:
        if parametros[1].isdigit():
            print("############################################################")
            print("empieza comunidades")
            print("############################################################")
            numero = int (parametros[1])
            comandos.mostrar_comunidades(grafo, numero)
        else:
            print("el parametro ",parametros[1],"no es un numero")
    elif comando == DIVULGAR:
        if parametros[2].isdigit():
            print("############################################################")
            print("empieza divulgar")
            print("############################################################")
            numero = int(parametros[2])
            comandos.divulgar_rumor(grafo ,parametros[1] , numero )
        else:
            print("el parametro ",parametros[2],"no es un numero")
    elif comando == DIVULGAR_CICLO:
        if parametros[2].isdigit():
            print("############################################################")
            print("empieza divulgar_ciclo")
            print("############################################################")
            comandos.divulgar_ciclo_n(grafo ,parametros[1] ,parametros[2])
        else:
            print("el parametro ",parametros[2],"no es un numero")
    elif comando == COM_FUERT_CONEXAS:      
        print("############################################################")
        print("empieza cfc")
        print("############################################################")
        comandos.componentes_fuert_conex(grafo)
    
def realizar_comandos(graf):
    
    for linea in sys.stdin:
        linea = procesar_linea(" ", linea)
        ejecutar_comando(linea[0],graf, linea)

def main():
    nom_archivo = sys.argv[1]
    graf = grafo.Grafo() 
    with open(nom_archivo) as archivo:
        cargar_vertices(archivo, graf)
    if len(graf):
        realizar_comandos(graf)

main()
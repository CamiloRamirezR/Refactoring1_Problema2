# Tenemos un archivo de logs que contiene errores, warnings y mensajes de información.
# Cada linea del archivo comienza con una letra que indica el tipo de log. Si
# comienza con 'E' es un error, si comienza con 'W' es un warning y si comienza
# con 'I' es de información. Luego de la letra, se encuentra un entero que
# indica el tiempo del log, y luego el mensaje del log. Excepto en el caso de
# los errores, que luego del tipo se encuentra un entero que indica la severidad
# del error. Por ejemplo:

# I 147 iniciando el programa
# W 604 this is not a warning
# E 2 4562 unexpected token

# Queremos separar los errores mas severos (con severidad mayor a 50) y ordenarlos
# cronologicamente. Despues, queremos imprimirlos a la pantalla.

import os

ERROR_FILE_PATH = './data/error.log'
ERROR_SEVERITY_THRESHOLD = 50
ERROR_SIGN = 'E'

def leer_archivo(path):
    with open(path, 'r') as f:
        lineas = f.readlines()
    return [line.rstrip().split(' ') for line in lineas]

def filtrar_errores(lineas):
    return [linea for linea in lineas if linea[0] == ERROR_SIGN and int(linea[1]) > ERROR_SEVERITY_THRESHOLD]

def organizar_errores(errores):
    return sorted(errores, key=lambda x: int(x[2]))

def imprimir_errores(errores):
    for error in errores:
        print(' '.join(error))


def organizar():
    lineas = leer_archivo(ERROR_FILE_PATH)
    errores = filtrar_errores(lineas)
    errores_ordenados = organizar_errores(errores)
    imprimir_errores(errores_ordenados)


def main():
    organizar()


if __name__ == '__main__':
    main()
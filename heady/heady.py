from itertools import islice
def leer_n_lineas_archivo(archivo, n=20):
    with open(archivo, 'r') as f:
        for l in islice(f, n):
            print(l, end='')
            
nombre_archivo = 'Alfonsina.txt'
n = 20
leer_n_lineas_archivo(nombre_archivo, n)




#crear un programa q se llame head.py que reciba un archivo
#y un numero N e imprima las primeras N lineas del archivo
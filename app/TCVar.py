
import numpy as np

Operadores = "unindids"
Conjuntos = "UABC"

# Conjuntos
U = np.arange(1, 10, 1)
# Los conjuntos A, B y C deben estar dentro de U
A = np.arange(1, 5, 1)
B = np.arange(2, 10, 2)
C = np.arange(3, 7, 1)

# Númer de operaciones
N_Un = 0  # uniones
N_I = 0  # intersecciones
N_D = 0  # diferencias
N_DS = 0  # diferencias simétricas
N_Total = 0  # total de operaciones
N_PP = 0  # Numero de pares de parentesis


def SolicitarConjunto(cadena):
    if 'A' in cadena:
        return A
    elif 'B' in cadena:
        return B
    elif 'C' in cadena:
        return C
    elif 'U' in cadena:
        return U

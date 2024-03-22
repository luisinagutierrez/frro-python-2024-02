"""Comparaciones Encadenadas, Cantidad Arbitraria de Parámetros, Recursividad."""

"""Toma 3 números y devuelve el máximo.

    Restricción: Utilizar UNICAMENTE tres IFs y comparaciones encadenadas.
    Referencia: https://docs.python.org/3/reference/expressions.html#comparisons
    """
def maximo_encadenado(a: float, b: float, c: float) -> float:
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    pass # Completar


# NO MODIFICAR - INICIO
assert maximo_encadenado(1, 10, 5) == 10
assert maximo_encadenado(4, 9, 18) == 18
assert maximo_encadenado(24, 9, 18) == 24
# NO MODIFICAR - FIN


###############################################################################

"""Re-escribir para que tome 4 parámetros, utilizar la función max.

    Referencia: https://docs.python.org/3/library/functions.html#max"""
def maximo_cuadruple(a: float, b: float, c: float, d: float) -> float:
    return max(a,b,c,d)
    pass # Completar


# NO MODIFICAR - INICIO
assert maximo_cuadruple(1, 10, 5, -5) == 10
assert maximo_cuadruple(4, 9, 18, 6) == 18
assert maximo_cuadruple(24, 9, 18, 20) == 24
assert maximo_cuadruple(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN


###############################################################################

"""Re-escribir para que tome una cantidad arbitraria de parámetros.
Referencia: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
"""
def maximo_arbitrario(*args) -> float:
    return max(args)            # Va sin * x error de sintaxis :)
    pass # Completar


# NO MODIFICAR - INICIO
assert maximo_arbitrario(1, 10, 5, -5) == 10
assert maximo_arbitrario(4, 9, 18, 6) == 18
assert maximo_arbitrario(24, 9, 18, 20) == 24
assert maximo_arbitrario(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN


###############################################################################
"""Re-Escribir de forma recursiva."""

def maximo_recursivo(*args) -> float:
    max_resto = maximo_recursivo(*args[1:])
    return args[0] if args[0] > max_resto else max_resto
    pass # Completar


# NO MODIFICAR - INICIO
assert maximo_recursivo(1, 10, 5, -5) == 10
assert maximo_recursivo(4, 9, 18, 6) == 18
assert maximo_recursivo(24, 9, 18, 20) == 24
assert maximo_recursivo(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN

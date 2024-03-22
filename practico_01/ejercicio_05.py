"""Bucle FOR y Reduce."""

from typing import Iterable

"""Toma un lista de números y devuelve el producto todos los númreos. Si
   la lista está vacia debe devolver 0.

   Restricciones: No usar bibliotecas auxiliares (Numpy, math, pandas).
   """
def multiplicar_basico(numeros: Iterable[float]) -> float:
    if len(numeros) == 0:
        return 0
    else:
        nro = 1
        for numero in numeros:
            nro *= numero
        return nro
    pass # Completar


# NO MODIFICAR - INICIO
assert multiplicar_basico([1, 2, 3, 4]) == 24
assert multiplicar_basico([2, 5]) == 10
assert multiplicar_basico([]) == 0
assert multiplicar_basico([1, 2, 3, 0, 4, 5]) == 0
assert multiplicar_basico(range(1, 20)) == 121_645_100_408_832_000
# NO MODIFICAR - FIN


###############################################################################


from functools import reduce

"""CHALLENGE OPCIONAL - Re-escribir utilizando reduce.
Referencia: https://docs.python.org/3.8/library/functools.html#functools.reduce
"""

def multiplicar_reduce(numeros: Iterable[float]) -> float:
    if len(numeros) != 0:
        nro: float = reduce(lambda x, y: x * y, numeros)
        return nro
    else:
        return 0
    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert multiplicar_reduce([1, 2, 3, 4]) == 24
    assert multiplicar_reduce([2, 5]) == 10
    assert multiplicar_reduce([]) == 0
    assert multiplicar_reduce([1, 2, 3, 0, 4, 5]) == 0
    assert multiplicar_reduce(range(1, 20)) == 121_645_100_408_832_000
# NO MODIFICAR - FIN

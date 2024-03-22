"""Any y Sets."""

from typing import Any, Iterable

"""Toma dos listas y devuelve un booleano en base a si tienen al menos 1
elemento en común.

Restricción: Utilizar bucles anidados.
"""

def superposicion_basico(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    for i in lista_1:
        for k in lista_2:
            if i == k:
                return True

    pass # Completar


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_basico(test_list, (2, "world", 35.20))
assert not superposicion_basico(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################
"""Re-Escribir utilizando un sólo bucle y el operador IN."""

def superposicion_in(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    for elemento in lista_1:
        if elemento in lista_2:
            return True
    pass # Completar


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_in(test_list, (2, "world", 35.20))
assert not superposicion_in(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################
"""Re-Escribir utilizando sin bucles, el operador in y la funcion any.
Referencia: https://docs.python.org/3/library/functions.html#any
"""

def superposicion_any(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    return any(x in lista_1 for x in lista_2)

    pass # Completar


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_any(test_list, (2, "world", 35.20))
assert not superposicion_any(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################
"""Re-Escribir utilizando conjuntos (sets).
Referencia: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
"""

def superposicion_set(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    set1= set(lista_1)
    set2= set(lista_2)
    if set1.intersection(set2):
        return True
    else:
        return False

    pass # Completar


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_set(test_list, (2, "world", 35.20))
assert not superposicion_set(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN

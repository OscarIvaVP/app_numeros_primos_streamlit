# -*- coding: utf-8 -*-
"""
Módulo de algoritmos para números primos
Contiene funciones para verificación, generación y análisis de números primos
"""

import math
import random
from typing import List, Dict, Tuple


# ==================== VERIFICACIÓN DE PRIMALIDAD ====================

def es_primo_basico(numero: int) -> bool:
    """
    Verifica si un número es primo usando división por prueba.

    Args:
        numero: Número entero a verificar

    Returns:
        True si es primo, False en caso contrario
    """
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False

    # Optimización: solo verificar divisores de la forma 6k ± 1
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True


def es_primo_con_pasos(numero: int) -> Tuple[bool, List[Dict]]:
    """
    Verifica si un número es primo y retorna los pasos del proceso.

    Args:
        numero: Número entero a verificar

    Returns:
        Tupla (es_primo, lista_de_pasos)
        Cada paso: {"divisor": int, "es_divisible": bool, "resto": int}
    """
    pasos = []

    if numero <= 1:
        return False, pasos
    if numero == 2:
        return True, pasos
    if numero % 2 == 0:
        pasos.append({"divisor": 2, "es_divisible": True, "resto": 0})
        return False, pasos

    limite = int(numero**0.5) + 1
    for i in range(2, min(limite, 100)):  # Limitar pasos para visualización
        resto = numero % i
        es_divisible = resto == 0
        pasos.append({
            "divisor": i,
            "es_divisible": es_divisible,
            "resto": resto
        })
        if es_divisible:
            return False, pasos

    # Si el número es grande y no encontramos divisor en los primeros 100
    if limite > 100:
        es_primo = es_primo_basico(numero)
        return es_primo, pasos

    return True, pasos


def es_primo_miller_rabin(n: int, k: int = 5) -> bool:
    """
    Test de primalidad de Miller-Rabin (probabilístico).
    Útil para números muy grandes.

    Args:
        n: Número a verificar
        k: Número de rondas (mayor k = mayor precisión)

    Returns:
        True si probablemente es primo, False si definitivamente es compuesto
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Escribir n-1 como 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Test de k rondas
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


# ==================== GENERACIÓN DE PRIMOS ====================

def criba_eratostenes(limite: int) -> List[int]:
    """
    Implementa la Criba de Eratóstenes para generar primos hasta un límite.

    Args:
        limite: Número máximo hasta el cual buscar primos

    Returns:
        Lista de números primos hasta el límite
    """
    if limite < 2:
        return []

    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False

    for i in range(2, int(limite**0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False

    return [num for num, primo in enumerate(es_primo) if primo]


def criba_eratostenes_pasos(limite: int) -> List[Dict]:
    """
    Genera los pasos de la Criba de Eratóstenes para animación.

    Args:
        limite: Número máximo hasta el cual ejecutar la criba

    Returns:
        Lista de diccionarios con el estado en cada paso
    """
    if limite < 2:
        return []

    pasos = []
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False

    # Registrar estado inicial
    pasos.append({
        "numero_actual": 2,
        "accion": "inicio",
        "estado": es_primo.copy()
    })

    for i in range(2, int(limite**0.5) + 1):
        if es_primo[i]:
            marcados = []
            for j in range(i * i, limite + 1, i):
                if es_primo[j]:
                    es_primo[j] = False
                    marcados.append(j)

            if marcados:
                pasos.append({
                    "numero_actual": i,
                    "accion": "marcar_multiplos",
                    "marcados": marcados,
                    "estado": es_primo.copy()
                })

    return pasos


def generar_primos_hasta(limite: int) -> List[int]:
    """
    Genera lista de números primos hasta un límite.
    Alias para criba_eratostenes.

    Args:
        limite: Número máximo

    Returns:
        Lista de primos
    """
    return criba_eratostenes(limite)


def primos_en_rango(inicio: int, fin: int) -> List[int]:
    """
    Encuentra todos los primos en un rango específico.

    Args:
        inicio: Número inicial del rango
        fin: Número final del rango

    Returns:
        Lista de primos en el rango [inicio, fin]
    """
    if fin < 2:
        return []

    # Generar todos los primos hasta fin y filtrar
    todos_primos = criba_eratostenes(fin)
    return [p for p in todos_primos if p >= inicio]


def enesimo_primo(n: int) -> int:
    """
    Encuentra el n-ésimo número primo.

    Args:
        n: Posición del primo buscado (1 = primer primo = 2)

    Returns:
        El n-ésimo número primo
    """
    if n < 1:
        return None

    # Estimación del límite superior usando aproximación
    if n < 6:
        limite = 15
    else:
        # Aproximación: el n-ésimo primo ≈ n * ln(n)
        limite = int(n * (math.log(n) + math.log(math.log(n)) + 2))

    while True:
        primos = criba_eratostenes(limite)
        if len(primos) >= n:
            return primos[n - 1]
        limite *= 2


def siguiente_primo(n: int) -> int:
    """
    Encuentra el siguiente número primo después de n.

    Args:
        n: Número de referencia

    Returns:
        Siguiente primo después de n
    """
    candidato = n + 1
    while not es_primo_basico(candidato):
        candidato += 1
    return candidato


def primo_anterior(n: int) -> int:
    """
    Encuentra el número primo anterior a n.

    Args:
        n: Número de referencia

    Returns:
        Primo anterior a n, o None si no existe
    """
    if n <= 2:
        return None

    candidato = n - 1
    while candidato > 1:
        if es_primo_basico(candidato):
            return candidato
        candidato -= 1

    return None


# ==================== FACTORIZACIÓN ====================

def factorizacion_prima(n: int) -> Dict[int, int]:
    """
    Calcula la factorización prima de un número.

    Args:
        n: Número a factorizar

    Returns:
        Diccionario {factor: exponente}
        Ejemplo: 60 -> {2: 2, 3: 1, 5: 1} porque 60 = 2² × 3 × 5
    """
    if n < 2:
        return {}

    factores = {}

    # Verificar factor 2
    while n % 2 == 0:
        factores[2] = factores.get(2, 0) + 1
        n //= 2

    # Verificar factores impares
    i = 3
    while i * i <= n:
        while n % i == 0:
            factores[i] = factores.get(i, 0) + 1
            n //= i
        i += 2

    # Si queda algo, es un factor primo
    if n > 2:
        factores[n] = factores.get(n, 0) + 1

    return factores


def factorizacion_con_proceso(n: int) -> Tuple[Dict[int, int], List[Dict]]:
    """
    Calcula la factorización prima y retorna el proceso paso a paso.

    Args:
        n: Número a factorizar

    Returns:
        Tupla (factores, pasos)
        - factores: Diccionario {factor: exponente}
        - pasos: Lista de diccionarios con cada paso de la división
    """
    if n < 2:
        return {}, []

    factores = {}
    pasos = []
    numero_actual = n

    # Factor 2
    while numero_actual % 2 == 0:
        factores[2] = factores.get(2, 0) + 1
        pasos.append({
            "divisor": 2,
            "numero_antes": numero_actual,
            "numero_despues": numero_actual // 2
        })
        numero_actual //= 2

    # Factores impares
    i = 3
    while i * i <= numero_actual:
        while numero_actual % i == 0:
            factores[i] = factores.get(i, 0) + 1
            pasos.append({
                "divisor": i,
                "numero_antes": numero_actual,
                "numero_despues": numero_actual // i
            })
            numero_actual //= i
        i += 2

    # Factor primo restante
    if numero_actual > 2:
        factores[numero_actual] = factores.get(numero_actual, 0) + 1
        pasos.append({
            "divisor": numero_actual,
            "numero_antes": numero_actual,
            "numero_despues": 1
        })

    return factores, pasos


# ==================== PROPIEDADES Y ANÁLISIS ====================

def contar_primos_hasta(n: int) -> int:
    """
    Función π(x): cuenta cuántos primos hay menores o iguales a n.

    Args:
        n: Límite superior

    Returns:
        Cantidad de primos ≤ n
    """
    if n < 2:
        return 0
    return len(criba_eratostenes(n))


def primos_gemelos(limite: int) -> List[Tuple[int, int]]:
    """
    Encuentra pares de primos gemelos hasta un límite.
    Primos gemelos: primos que difieren en 2 (ej: 3 y 5, 11 y 13)

    Args:
        limite: Número máximo para buscar

    Returns:
        Lista de tuplas (p, p+2) donde ambos son primos
    """
    primos = criba_eratostenes(limite)
    gemelos = []

    for i in range(len(primos) - 1):
        if primos[i + 1] - primos[i] == 2:
            gemelos.append((primos[i], primos[i + 1]))

    return gemelos


def es_potencia_de_primo(n: int) -> Tuple[bool, int, int]:
    """
    Verifica si un número es potencia de un primo.

    Args:
        n: Número a verificar

    Returns:
        Tupla (es_potencia, base, exponente)
        Si es potencia: (True, p, k) donde n = p^k
        Si no: (False, 0, 0)
    """
    if n < 2:
        return False, 0, 0

    factores = factorizacion_prima(n)

    # Si hay exactamente un factor primo, es potencia de primo
    if len(factores) == 1:
        base = list(factores.keys())[0]
        exponente = factores[base]
        return True, base, exponente

    return False, 0, 0


def distancia_primo_mas_cercano(n: int) -> Dict:
    """
    Encuentra la distancia al primo más cercano.

    Args:
        n: Número de referencia

    Returns:
        Diccionario con información del primo más cercano
    """
    if es_primo_basico(n):
        return {
            "es_primo": True,
            "distancia": 0,
            "primo_mas_cercano": n
        }

    sig = siguiente_primo(n)
    ant = primo_anterior(n)

    if ant is None:
        return {
            "es_primo": False,
            "distancia": sig - n,
            "primo_mas_cercano": sig,
            "direccion": "siguiente"
        }

    dist_sig = sig - n
    dist_ant = n - ant

    if dist_sig <= dist_ant:
        return {
            "es_primo": False,
            "distancia": dist_sig,
            "primo_mas_cercano": sig,
            "direccion": "siguiente"
        }
    else:
        return {
            "es_primo": False,
            "distancia": dist_ant,
            "primo_mas_cercano": ant,
            "direccion": "anterior"
        }

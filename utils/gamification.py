# -*- coding: utf-8 -*-
"""
Módulo de gamificación para la aplicación de números primos
Contiene quiz, retos y sistema de puntuación
"""

import random
from typing import Dict, Tuple, List


# ==================== PREGUNTAS DE QUIZ ====================

PREGUNTAS_FACILES = [
    {
        "pregunta": "¿Cuál es el primer número primo?",
        "opciones": ["1", "2", "3", "4"],
        "respuesta_correcta": "2",
        "explicacion": "2 es el primer número primo y el único primo par."
    },
    {
        "pregunta": "¿Es 1 un número primo?",
        "opciones": ["Sí", "No"],
        "respuesta_correcta": "No",
        "explicacion": "1 no es primo porque un primo debe tener exactamente dos divisores distintos."
    },
    {
        "pregunta": "¿Cuál de estos números es primo?",
        "opciones": ["4", "6", "7", "9"],
        "respuesta_correcta": "7",
        "explicacion": "7 solo es divisible por 1 y 7, por lo tanto es primo."
    },
    {
        "pregunta": "¿Es 2 el único número primo par?",
        "opciones": ["Sí", "No"],
        "respuesta_correcta": "Sí",
        "explicacion": "Todos los demás números pares son divisibles por 2, por lo tanto no son primos."
    },
    {
        "pregunta": "¿Cuántos números primos hay menores que 10?",
        "opciones": ["3", "4", "5", "6"],
        "respuesta_correcta": "4",
        "explicacion": "Los primos menores que 10 son: 2, 3, 5 y 7."
    },
    {
        "pregunta": "¿Es 9 un número primo?",
        "opciones": ["Sí", "No"],
        "respuesta_correcta": "No",
        "explicacion": "9 = 3 × 3, por lo tanto no es primo."
    },
    {
        "pregunta": "¿Cuál es el primo más cercano a 20?",
        "opciones": ["17", "19", "21", "23"],
        "respuesta_correcta": "19",
        "explicacion": "19 es primo y está más cerca de 20 que 17 o 23."
    }
]

PREGUNTAS_MEDIAS = [
    {
        "pregunta": "¿Cuál es el décimo número primo?",
        "opciones": ["23", "27", "29", "31"],
        "respuesta_correcta": "29",
        "explicacion": "Los primeros 10 primos son: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29."
    },
    {
        "pregunta": "¿Qué son los números primos gemelos?",
        "opciones": [
            "Primos que suman lo mismo",
            "Primos que difieren en 2",
            "Primos que son iguales",
            "Primos consecutivos"
        ],
        "respuesta_correcta": "Primos que difieren en 2",
        "explicacion": "Los primos gemelos son pares de primos que difieren en 2, como (3,5), (11,13), (17,19)."
    },
    {
        "pregunta": "¿Cuál es la Criba de Eratóstenes?",
        "opciones": [
            "Un método para sumar primos",
            "Un método para encontrar primos",
            "Un tipo de número primo",
            "Una fórmula matemática"
        ],
        "respuesta_correcta": "Un método para encontrar primos",
        "explicacion": "La Criba de Eratóstenes es un algoritmo antiguo para encontrar todos los primos hasta un límite."
    },
    {
        "pregunta": "¿Cuál de estos NO es un par de primos gemelos?",
        "opciones": ["(3, 5)", "(5, 7)", "(11, 13)", "(13, 15)"],
        "respuesta_correcta": "(13, 15)",
        "explicacion": "15 = 3 × 5, por lo tanto no es primo."
    },
    {
        "pregunta": "¿Cuántos primos hay entre 10 y 20?",
        "opciones": ["3", "4", "5", "6"],
        "respuesta_correcta": "4",
        "explicacion": "Los primos entre 10 y 20 son: 11, 13, 17 y 19."
    },
    {
        "pregunta": "¿Cuál es el mayor primo menor que 100?",
        "opciones": ["91", "93", "97", "99"],
        "respuesta_correcta": "97",
        "explicacion": "97 es el mayor número primo menor que 100."
    }
]

PREGUNTAS_DIFICILES = [
    {
        "pregunta": "¿Quién demostró que existen infinitos números primos?",
        "opciones": ["Pitágoras", "Euclides", "Eratóstenes", "Fermat"],
        "respuesta_correcta": "Euclides",
        "explicacion": "Euclides demostró la infinitud de los primos alrededor del 300 a.C."
    },
    {
        "pregunta": "¿Qué es un primo de Mersenne?",
        "opciones": [
            "Un primo de la forma 2^p - 1",
            "Un primo de la forma p^2 + 1",
            "Un primo muy grande",
            "Un primo francés"
        ],
        "respuesta_correcta": "Un primo de la forma 2^p - 1",
        "explicacion": "Los primos de Mersenne tienen la forma 2^p - 1, donde p también es primo."
    },
    {
        "pregunta": "¿Cuál es la complejidad del algoritmo de división por prueba para verificar primalidad?",
        "opciones": ["O(n)", "O(√n)", "O(log n)", "O(n²)"],
        "respuesta_correcta": "O(√n)",
        "explicacion": "Solo necesitamos verificar divisores hasta la raíz cuadrada de n."
    },
    {
        "pregunta": "¿Qué aproxima la función π(x)?",
        "opciones": [
            "La cantidad de primos menores o iguales a x",
            "El x-ésimo número primo",
            "La suma de primos hasta x",
            "El producto de primos hasta x"
        ],
        "respuesta_correcta": "La cantidad de primos menores o iguales a x",
        "explicacion": "π(x) es la función que cuenta cuántos primos hay ≤ x."
    },
    {
        "pregunta": "¿Qué es el Teorema Fundamental de la Aritmética?",
        "opciones": [
            "Todo número es primo o compuesto",
            "Hay infinitos primos",
            "Todo número >1 se factoriza únicamente en primos",
            "Los primos son impredecibles"
        ],
        "respuesta_correcta": "Todo número >1 se factoriza únicamente en primos",
        "explicacion": "Establece que cada número tiene una factorización prima única (salvo el orden)."
    },
    {
        "pregunta": "¿Cuál es el algoritmo de primalidad determinista y polinomial descubierto en 2002?",
        "opciones": ["Miller-Rabin", "Fermat", "AKS", "Solovay-Strassen"],
        "respuesta_correcta": "AKS",
        "explicacion": "El test AKS (Agrawal-Kayal-Saxena) fue el primer algoritmo determinista polinomial."
    }
]


# ==================== FUNCIONES DE QUIZ ====================

def generar_pregunta_quiz(nivel: str = "facil") -> Dict:
    """
    Genera una pregunta aleatoria de quiz según el nivel.

    Args:
        nivel: 'facil', 'medio', o 'dificil'

    Returns:
        Diccionario con la pregunta, opciones y respuesta correcta
    """
    if nivel == "facil":
        preguntas = PREGUNTAS_FACILES
    elif nivel == "medio":
        preguntas = PREGUNTAS_MEDIAS
    elif nivel == "dificil":
        preguntas = PREGUNTAS_DIFICILES
    else:
        preguntas = PREGUNTAS_FACILES

    return random.choice(preguntas)


def verificar_respuesta(pregunta: Dict, respuesta_usuario: str) -> Tuple[bool, str]:
    """
    Verifica si la respuesta del usuario es correcta.

    Args:
        pregunta: Diccionario con la pregunta
        respuesta_usuario: Respuesta dada por el usuario

    Returns:
        Tupla (es_correcta, explicación)
    """
    es_correcta = respuesta_usuario == pregunta["respuesta_correcta"]
    return es_correcta, pregunta["explicacion"]


def calcular_puntuacion(tiempo_segundos: float, nivel: str, es_correcta: bool) -> int:
    """
    Calcula la puntuación basada en tiempo, nivel y corrección.

    Args:
        tiempo_segundos: Tiempo que tomó responder
        nivel: Nivel de dificultad
        es_correcta: Si la respuesta fue correcta

    Returns:
        Puntuación obtenida
    """
    if not es_correcta:
        return 0

    # Puntos base según nivel
    puntos_base = {
        "facil": 10,
        "medio": 20,
        "dificil": 30
    }

    puntos = puntos_base.get(nivel, 10)

    # Bonus por velocidad (máximo 10 puntos extra)
    if tiempo_segundos < 5:
        puntos += 10
    elif tiempo_segundos < 10:
        puntos += 5
    elif tiempo_segundos < 20:
        puntos += 2

    return puntos


# ==================== DESAFÍOS ====================

def generar_desafio_aleatorio() -> Dict:
    """
    Genera un desafío matemático aleatorio.

    Returns:
        Diccionario con el desafío, respuesta correcta y tipo
    """
    desafios = [
        {
            "tipo": "encontrar_primo",
            "descripcion": "¿Cuál es el siguiente primo después de {}?",
            "generar": lambda: random.randint(10, 100)
        },
        {
            "tipo": "contar_primos",
            "descripcion": "¿Cuántos primos hay entre {} y {}?",
            "generar": lambda: (random.randint(10, 50), random.randint(51, 100))
        },
        {
            "tipo": "es_primo",
            "descripcion": "¿El número {} es primo?",
            "generar": lambda: random.randint(50, 150)
        },
        {
            "tipo": "factorizar",
            "descripcion": "¿Cuál es el factor primo más grande de {}?",
            "generar": lambda: random.randint(20, 100)
        }
    ]

    desafio_template = random.choice(desafios)
    parametros = desafio_template["generar"]()

    if desafio_template["tipo"] == "contar_primos":
        descripcion = desafio_template["descripcion"].format(*parametros)
    else:
        descripcion = desafio_template["descripcion"].format(parametros)

    return {
        "tipo": desafio_template["tipo"],
        "descripcion": descripcion,
        "parametros": parametros
    }


# ==================== LOGROS ====================

def verificar_logros(estadisticas: Dict) -> List[Dict]:
    """
    Verifica qué logros ha conseguido el usuario.

    Args:
        estadisticas: Diccionario con estadísticas del usuario

    Returns:
        Lista de logros conseguidos
    """
    logros = []

    # Logros por cantidad de verificaciones
    verificaciones = estadisticas.get("verificaciones", 0)
    if verificaciones >= 10:
        logros.append({
            "nombre": "Explorador de Primos",
            "descripcion": "Verificaste 10 números",
            "icono": "🔍"
        })
    if verificaciones >= 50:
        logros.append({
            "nombre": "Cazador de Primos",
            "descripcion": "Verificaste 50 números",
            "icono": "🎯"
        })
    if verificaciones >= 100:
        logros.append({
            "nombre": "Maestro de Primos",
            "descripcion": "Verificaste 100 números",
            "icono": "👑"
        })

    # Logros por puntuación en quiz
    puntuacion_quiz = estadisticas.get("puntuacion_quiz", 0)
    if puntuacion_quiz >= 50:
        logros.append({
            "nombre": "Estudiante Aplicado",
            "descripcion": "Conseguiste 50 puntos en el quiz",
            "icono": "📚"
        })
    if puntuacion_quiz >= 200:
        logros.append({
            "nombre": "Erudito Matemático",
            "descripcion": "Conseguiste 200 puntos en el quiz",
            "icono": "🎓"
        })

    # Logros especiales
    if estadisticas.get("primo_mas_grande_encontrado", 0) > 1000:
        logros.append({
            "nombre": "Buscador de Gigantes",
            "descripcion": "Verificaste un número >1000",
            "icono": "🗿"
        })

    return logros


def obtener_titulo_usuario(puntuacion_total: int) -> Tuple[str, str]:
    """
    Determina el título del usuario según su puntuación total.

    Args:
        puntuacion_total: Puntuación acumulada

    Returns:
        Tupla (título, icono)
    """
    if puntuacion_total < 50:
        return "Aprendiz", "🌱"
    elif puntuacion_total < 150:
        return "Estudiante", "📖"
    elif puntuacion_total < 300:
        return "Matemático", "🔢"
    elif puntuacion_total < 500:
        return "Experto", "⭐"
    else:
        return "Gran Maestro", "🏆"


# ==================== RETOS CRONOMETRADOS ====================

RETOS_RAPIDOS = [
    {
        "pregunta": "Escribe el 5to número primo",
        "respuesta": "11",
        "tiempo_limite": 10
    },
    {
        "pregunta": "¿Cuántos primos hay menores que 20?",
        "respuesta": "8",
        "tiempo_limite": 15
    },
    {
        "pregunta": "Escribe un primo gemelo de 5",
        "respuesta": ["3", "7"],
        "tiempo_limite": 10
    },
    {
        "pregunta": "¿Es 91 primo? (sí/no)",
        "respuesta": "no",
        "tiempo_limite": 15
    }
]


def generar_reto_rapido() -> Dict:
    """
    Genera un reto cronometrado aleatorio.

    Returns:
        Diccionario con el reto
    """
    return random.choice(RETOS_RAPIDOS)


def verificar_reto_rapido(reto: Dict, respuesta: str, tiempo_usado: float) -> Tuple[bool, int]:
    """
    Verifica un reto rápido.

    Args:
        reto: Diccionario del reto
        respuesta: Respuesta del usuario
        tiempo_usado: Tiempo que tardó en responder

    Returns:
        Tupla (es_correcta, puntos_ganados)
    """
    respuesta = respuesta.strip().lower()
    respuesta_correcta = reto["respuesta"]

    # Manejar múltiples respuestas válidas
    if isinstance(respuesta_correcta, list):
        es_correcta = respuesta in [r.lower() for r in respuesta_correcta]
    else:
        es_correcta = respuesta == respuesta_correcta.lower()

    if not es_correcta:
        return False, 0

    # Calcular puntos según velocidad
    tiempo_limite = reto["tiempo_limite"]
    if tiempo_usado <= tiempo_limite * 0.5:
        puntos = 30
    elif tiempo_usado <= tiempo_limite * 0.75:
        puntos = 20
    elif tiempo_usado <= tiempo_limite:
        puntos = 10
    else:
        puntos = 5  # Respondió correctamente pero fuera de tiempo

    return True, puntos

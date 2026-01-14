# -*- coding: utf-8 -*-
"""
Módulo de visualizaciones para números primos
Contiene funciones para crear gráficos interactivos con Plotly
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import math


def grafico_distribucion_primos(limite: int, primos: list):
    """
    Crea un gráfico de distribución de números primos.

    Args:
        limite: Número máximo considerado
        primos: Lista de números primos

    Returns:
        Figura de Plotly
    """
    # Crear bins para agrupar
    num_bins = min(50, limite // 10)
    bins = np.linspace(0, limite, num_bins)
    counts, edges = np.histogram(primos, bins=bins)

    # Crear figura
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=edges[:-1],
        y=counts,
        name='Primos',
        marker_color='#1f77b4',
        hovertemplate='Rango: %{x:.0f}<br>Cantidad: %{y}<extra></extra>'
    ))

    fig.update_layout(
        title=f'Distribución de Números Primos hasta {limite}',
        xaxis_title='Rango de números',
        yaxis_title='Cantidad de primos',
        hovermode='x unified',
        template='plotly_white'
    )

    return fig


def grafico_funcion_pi(limite: int, primos: list):
    """
    Crea gráfico de la función π(x) vs aproximación x/ln(x).

    Args:
        limite: Límite superior
        primos: Lista de números primos

    Returns:
        Figura de Plotly
    """
    # Generar valores de x
    x_values = list(range(2, limite + 1, max(1, limite // 1000)))

    # Calcular π(x) - cantidad de primos hasta x
    pi_values = [sum(1 for p in primos if p <= x) for x in x_values]

    # Calcular aproximación x/ln(x)
    aprox_values = [x / np.log(x) for x in x_values]

    # Crear DataFrame
    df = pd.DataFrame({
        'x': x_values,
        'π(x)': pi_values,
        'x/ln(x)': aprox_values
    })

    # Crear figura
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['x'],
        y=df['π(x)'],
        mode='lines',
        name='π(x) - Cantidad real de primos',
        line=dict(color='#1f77b4', width=2),
        hovertemplate='x: %{x}<br>π(x): %{y}<extra></extra>'
    ))

    fig.add_trace(go.Scatter(
        x=df['x'],
        y=df['x/ln(x)'],
        mode='lines',
        name='x/ln(x) - Aproximación',
        line=dict(color='#ff7f0e', width=2, dash='dash'),
        hovertemplate='x: %{x}<br>Aproximación: %{y:.1f}<extra></extra>'
    ))

    fig.update_layout(
        title='Función π(x): Conteo de Primos vs Aproximación',
        xaxis_title='x',
        yaxis_title='Cantidad de primos',
        hovermode='x unified',
        template='plotly_white',
        legend=dict(x=0.02, y=0.98)
    )

    return fig


def espiral_ulam(dimension: int, primos: list):
    """
    Crea una Espiral de Ulam destacando números primos.

    Args:
        dimension: Dimensión de la espiral (debe ser impar)
        primos: Lista de números primos

    Returns:
        Figura de Plotly
    """
    # Asegurar dimensión impar
    if dimension % 2 == 0:
        dimension += 1

    # Crear matriz
    matriz = np.zeros((dimension, dimension))
    primos_set = set(primos)

    # Generar espiral
    x, y = dimension // 2, dimension // 2
    dx, dy = 0, -1
    numero = 1

    for _ in range(dimension ** 2):
        if 0 <= x < dimension and 0 <= y < dimension:
            matriz[y][x] = 1 if numero in primos_set else 0
            numero += 1

        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx

        x, y = x + dx, y + dy

    # Crear heatmap
    fig = go.Figure(data=go.Heatmap(
        z=matriz,
        colorscale=[[0, '#f0f0f0'], [1, '#1f77b4']],
        showscale=False,
        hovertemplate='<extra></extra>'
    ))

    fig.update_layout(
        title=f'Espiral de Ulam ({dimension}×{dimension})',
        xaxis=dict(showticklabels=False, showgrid=False),
        yaxis=dict(showticklabels=False, showgrid=False),
        width=600,
        height=600,
        template='plotly_white'
    )

    return fig


def comparacion_primos_compuestos(limite: int, primos: list):
    """
    Crea gráfico comparativo de primos vs compuestos.

    Args:
        limite: Límite superior
        primos: Lista de números primos

    Returns:
        Figura de Plotly
    """
    cantidad_primos = len(primos)
    cantidad_compuestos = limite - cantidad_primos - 1  # -1 por el 1

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=['Números Primos', 'Números Compuestos'],
        y=[cantidad_primos, cantidad_compuestos],
        marker_color=['#1f77b4', '#ff7f0e'],
        text=[cantidad_primos, cantidad_compuestos],
        textposition='auto',
        hovertemplate='%{x}<br>Cantidad: %{y}<extra></extra>'
    ))

    fig.update_layout(
        title=f'Primos vs Compuestos (hasta {limite})',
        yaxis_title='Cantidad',
        template='plotly_white',
        showlegend=False
    )

    return fig


def visualizar_factorizacion(n: int, factores: dict):
    """
    Crea visualización de la factorización prima.

    Args:
        n: Número factorizado
        factores: Diccionario {factor: exponente}

    Returns:
        Figura de Plotly
    """
    if not factores:
        return None

    # Preparar datos
    factores_list = []
    exponentes_list = []
    contribucion_list = []

    for factor, exponente in sorted(factores.items()):
        factores_list.append(f"{factor}")
        exponentes_list.append(exponente)
        contribucion_list.append(factor ** exponente)

    # Crear figura
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=factores_list,
        y=contribucion_list,
        text=[f"{factor}^{exp}" if exp > 1 else f"{factor}"
              for factor, exp in zip(factores_list, exponentes_list)],
        textposition='auto',
        marker_color='#2ca02c',
        hovertemplate='Factor: %{x}<br>Contribución: %{y}<extra></extra>'
    ))

    # Crear expresión de factorización
    expresion = " × ".join([f"{f}^{e}" if e > 1 else f"{f}"
                            for f, e in sorted(factores.items())])

    fig.update_layout(
        title=f'Factorización Prima de {n} = {expresion}',
        xaxis_title='Factores Primos',
        yaxis_title='Contribución (factor^exponente)',
        template='plotly_white'
    )

    return fig


def heatmap_criba(estado: list, dimension: int):
    """
    Crea un heatmap para visualizar el estado de la Criba de Eratóstenes.

    Args:
        estado: Lista booleana indicando si cada número es primo
        dimension: Dimensión de la cuadrícula

    Returns:
        Figura de Plotly
    """
    # Calcular dimensiones de la matriz
    n_elementos = len(estado)
    cols = dimension
    rows = math.ceil(n_elementos / cols)

    # Crear matriz
    matriz = np.zeros((rows, cols))
    for i, es_primo in enumerate(estado):
        if i < n_elementos:
            row = i // cols
            col = i % cols
            matriz[row][col] = 1 if es_primo else 0

    # Crear anotaciones con los números
    annotations = []
    for i in range(n_elementos):
        row = i // cols
        col = i % cols
        color = 'white' if estado[i] else 'black'
        annotations.append(
            dict(
                x=col,
                y=row,
                text=str(i),
                showarrow=False,
                font=dict(color=color, size=10)
            )
        )

    # Crear heatmap
    fig = go.Figure(data=go.Heatmap(
        z=matriz,
        colorscale=[[0, '#e74c3c'], [1, '#27ae60']],
        showscale=False,
        hovertemplate='Número: %{text}<extra></extra>',
        text=[[str(i + j * cols) if (i + j * cols) < n_elementos else ''
               for i in range(cols)] for j in range(rows)]
    ))

    fig.update_layout(
        title='Estado de la Criba de Eratóstenes',
        xaxis=dict(showticklabels=False, showgrid=False),
        yaxis=dict(showticklabels=False, showgrid=False),
        annotations=annotations,
        width=800,
        height=600,
        template='plotly_white'
    )

    return fig


def grafico_brechas_primos(primos: list):
    """
    Visualiza las brechas entre números primos consecutivos.

    Args:
        primos: Lista de números primos

    Returns:
        Figura de Plotly
    """
    if len(primos) < 2:
        return None

    # Calcular brechas
    brechas = [primos[i + 1] - primos[i] for i in range(len(primos) - 1)]
    posiciones = primos[:-1]

    # Crear figura
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=posiciones,
        y=brechas,
        mode='markers',
        marker=dict(
            size=5,
            color=brechas,
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Brecha")
        ),
        hovertemplate='Primo: %{x}<br>Brecha al siguiente: %{y}<extra></extra>'
    ))

    fig.update_layout(
        title='Brechas entre Números Primos Consecutivos',
        xaxis_title='Número Primo',
        yaxis_title='Brecha al siguiente primo',
        template='plotly_white'
    )

    return fig


def grafico_estadisticas_sesion(historial: list):
    """
    Crea gráfico de estadísticas de la sesión.

    Args:
        historial: Lista de números verificados

    Returns:
        Figura de Plotly
    """
    if not historial:
        return None

    # Contar frecuencias
    from collections import Counter
    contador = Counter(historial)
    numeros = list(contador.keys())
    frecuencias = list(contador.values())

    # Ordenar por frecuencia
    datos = sorted(zip(numeros, frecuencias), key=lambda x: x[1], reverse=True)[:10]
    numeros_top = [str(d[0]) for d in datos]
    frecuencias_top = [d[1] for d in datos]

    # Crear figura
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=numeros_top,
        y=frecuencias_top,
        marker_color='#9467bd',
        text=frecuencias_top,
        textposition='auto',
        hovertemplate='Número: %{x}<br>Veces verificado: %{y}<extra></extra>'
    ))

    fig.update_layout(
        title='Top 10 Números Más Verificados',
        xaxis_title='Número',
        yaxis_title='Veces verificado',
        template='plotly_white'
    )

    return fig

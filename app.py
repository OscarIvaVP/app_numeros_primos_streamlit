# -*- coding: utf-8 -*-
"""
Academia Interactiva de Números Primos
Aplicación educativa completa sobre teoría de números primos
"""

import streamlit as st
import time
import pandas as pd
from datetime import datetime

# Importar módulos personalizados
from utils.prime_algorithms import (
    es_primo_basico, es_primo_con_pasos, criba_eratostenes,
    criba_eratostenes_pasos, primos_en_rango, enesimo_primo,
    factorizacion_prima, factorizacion_con_proceso,
    contar_primos_hasta, primos_gemelos, distancia_primo_mas_cercano
)
from utils.visualizations import (
    grafico_distribucion_primos, grafico_funcion_pi, espiral_ulam,
    comparacion_primos_compuestos, visualizar_factorizacion,
    heatmap_criba, grafico_brechas_primos, grafico_estadisticas_sesion
)
from utils.gamification import (
    generar_pregunta_quiz, verificar_respuesta, calcular_puntuacion,
    verificar_logros, obtener_titulo_usuario
)
from utils.educational_content import (
    obtener_teoria_basica, obtener_historia_primos,
    obtener_aplicaciones_reales, obtener_teoremas_importantes,
    comparacion_algoritmos, obtener_curiosidades
)


# ==================== CONFIGURACIÓN ====================

st.set_page_config(
    page_title="Academia de Números Primos",
    page_icon="🔢",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================== CSS PERSONALIZADO ====================

def load_custom_css():
    """Carga estilos CSS personalizados"""
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        background: linear-gradient(90deg, #1f77b4, #2ca02c);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        background-color: #f0f2f6;
        border-radius: 5px;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)


# ==================== INICIALIZACIÓN ====================

def init_session_state():
    """Inicializa el estado de la sesión"""
    if 'verificaciones' not in st.session_state:
        st.session_state.verificaciones = 0
    if 'historial' not in st.session_state:
        st.session_state.historial = []
    if 'puntuacion_quiz' not in st.session_state:
        st.session_state.puntuacion_quiz = 0
    if 'respuestas_correctas' not in st.session_state:
        st.session_state.respuestas_correctas = 0
    if 'respuestas_incorrectas' not in st.session_state:
        st.session_state.respuestas_incorrectas = 0
    if 'primo_mas_grande_encontrado' not in st.session_state:
        st.session_state.primo_mas_grande_encontrado = 0
    if 'pregunta_actual' not in st.session_state:
        st.session_state.pregunta_actual = None
    if 'tiempo_pregunta' not in st.session_state:
        st.session_state.tiempo_pregunta = None


# ==================== CACHÉ DE FUNCIONES ====================

@st.cache_data
def calcular_primos_cached(limite):
    """Calcula primos con caché"""
    return criba_eratostenes(limite)


# ==================== SIDEBAR ====================

def render_sidebar():
    """Renderiza el sidebar con información y estadísticas"""
    with st.sidebar:
        st.markdown("### 📊 Estadísticas de Sesión")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Verificaciones", st.session_state.verificaciones)
        with col2:
            st.metric("Puntos Quiz", st.session_state.puntuacion_quiz)

        # Título del usuario
        titulo, icono = obtener_titulo_usuario(st.session_state.puntuacion_quiz)
        st.markdown(f"**Rango:** {icono} {titulo}")

        st.markdown("---")

        # Información adicional
        st.markdown("### ℹ️ Información")
        st.info("Esta aplicación te permite explorar el fascinante mundo de los números primos de forma interactiva.")

        st.markdown("### 🎯 Logros")
        estadisticas = {
            "verificaciones": st.session_state.verificaciones,
            "puntuacion_quiz": st.session_state.puntuacion_quiz,
            "primo_mas_grande_encontrado": st.session_state.primo_mas_grande_encontrado
        }
        logros = verificar_logros(estadisticas)

        if logros:
            for logro in logros[:3]:  # Mostrar máximo 3
                st.success(f"{logro['icono']} **{logro['nombre']}**")
        else:
            st.write("¡Comienza a explorar para desbloquear logros!")

        # Reset button
        if st.button("🔄 Reiniciar Estadísticas"):
            st.session_state.verificaciones = 0
            st.session_state.historial = []
            st.session_state.puntuacion_quiz = 0
            st.session_state.respuestas_correctas = 0
            st.session_state.respuestas_incorrectas = 0
            st.session_state.primo_mas_grande_encontrado = 0
            st.rerun()


# ==================== TAB 1: VERIFICADOR ====================

def tab_verificador():
    """Tab principal de verificación de números primos"""
    st.header("🏠 Verificador de Números Primos")

    col1, col2 = st.columns([2, 1])

    with col1:
        numero = st.number_input(
            "Ingresa un número entero:",
            min_value=0,
            max_value=1000000,
            value=17,
            step=1
        )

    with col2:
        st.write("")
        st.write("")
        verificar = st.button("🔍 Verificar", use_container_width=True, type="primary")

    if verificar:
        st.session_state.verificaciones += 1
        st.session_state.historial.append(numero)

        inicio = time.time()
        es_primo = es_primo_basico(numero)
        tiempo_ms = (time.time() - inicio) * 1000

        # Actualizar primo más grande
        if es_primo and numero > st.session_state.primo_mas_grande_encontrado:
            st.session_state.primo_mas_grande_encontrado = numero

        # Resultado principal
        if es_primo:
            st.success(f"✅ ¡El número **{numero}** SÍ es un número primo!")
        else:
            st.error(f"❌ El número **{numero}** NO es un número primo.")

        # Métricas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Número Evaluado", numero)
        with col2:
            st.metric("Resultado", "PRIMO" if es_primo else "COMPUESTO")
        with col3:
            st.metric("Tiempo", f"{tiempo_ms:.2f} ms")

        # Análisis detallado para compuestos
        if not es_primo and numero > 1:
            st.markdown("---")
            st.subheader("📊 Factorización Prima")

            factores, pasos = factorizacion_con_proceso(numero)

            if factores:
                # Mostrar factorización
                expresion = " × ".join([
                    f"{f}^{e}" if e > 1 else f"{f}"
                    for f, e in sorted(factores.items())
                ])
                st.info(f"**{numero} = {expresion}**")

                # Visualización
                fig = visualizar_factorizacion(numero, factores)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)

                # Tabla de pasos
                if st.checkbox("Ver proceso de factorización"):
                    df_pasos = pd.DataFrame(pasos)
                    st.dataframe(df_pasos, use_container_width=True)

        # Análisis adicional
        if numero > 1:
            st.markdown("---")
            st.subheader("🔎 Análisis Adicional")

            info_distancia = distancia_primo_mas_cercano(numero)

            col1, col2 = st.columns(2)
            with col1:
                if not es_primo:
                    st.write(f"**Primo más cercano:** {info_distancia['primo_mas_cercano']}")
                    st.write(f"**Distancia:** {info_distancia['distancia']}")

            with col2:
                # Verificar si es parte de un par gemelo
                if es_primo:
                    gemelos = primos_gemelos(numero + 10)
                    for par in gemelos:
                        if numero in par:
                            st.success(f"¡Es parte del par gemelo {par}!")
                            break


# ==================== TAB 2: VISUALIZACIONES ====================

def tab_visualizaciones():
    """Tab de visualizaciones interactivas"""
    st.header("📊 Visualizaciones Interactivas")

    st.markdown("Explora patrones visuales de números primos con gráficos interactivos.")

    # Selector de visualización
    tipo_viz = st.selectbox(
        "Selecciona una visualización:",
        ["Distribución de Primos", "Función π(x)", "Espiral de Ulam",
         "Comparación Primos vs Compuestos", "Brechas entre Primos"]
    )

    # Controles según el tipo
    if tipo_viz in ["Distribución de Primos", "Función π(x)", "Comparación Primos vs Compuestos", "Brechas entre Primos"]:
        limite = st.slider("Límite superior:", 10, 10000, 1000, 10)

        with st.spinner("Calculando primos..."):
            primos = calcular_primos_cached(limite)

        if tipo_viz == "Distribución de Primos":
            fig = grafico_distribucion_primos(limite, primos)
            st.plotly_chart(fig, use_container_width=True)
            st.info(f"Se encontraron **{len(primos)}** números primos hasta {limite}.")

        elif tipo_viz == "Función π(x)":
            fig = grafico_funcion_pi(limite, primos)
            st.plotly_chart(fig, use_container_width=True)
            st.info(f"π({limite}) = {len(primos)}")

        elif tipo_viz == "Comparación Primos vs Compuestos":
            fig = comparacion_primos_compuestos(limite, primos)
            st.plotly_chart(fig, use_container_width=True)

        elif tipo_viz == "Brechas entre Primos":
            if len(primos) > 1:
                fig = grafico_brechas_primos(primos)
                st.plotly_chart(fig, use_container_width=True)

    elif tipo_viz == "Espiral de Ulam":
        dimension = st.slider("Dimensión de la espiral:", 11, 101, 51, 2)

        with st.spinner("Generando espiral de Ulam..."):
            limite_espiral = dimension ** 2
            primos = calcular_primos_cached(limite_espiral)
            fig = espiral_ulam(dimension, primos)
            st.plotly_chart(fig, use_container_width=True)

        st.info("La Espiral de Ulam muestra patrones sorprendentes en la distribución de primos. Los números primos aparecen en azul.")


# ==================== TAB 3: CRIBA DE ERATÓSTENES ====================

def tab_criba():
    """Tab de Criba de Eratóstenes animada"""
    st.header("🎨 Criba de Eratóstenes")

    # Explicación
    with st.expander("📖 ¿Qué es la Criba de Eratóstenes?"):
        st.markdown("""
        La **Criba de Eratóstenes** es un algoritmo antiguo y eficiente para encontrar todos los números primos hasta un límite dado.

        **Algoritmo:**
        1. Crear una lista de números desde 2 hasta n
        2. Empezar con el primer número (2)
        3. Marcar todos sus múltiplos como compuestos
        4. Pasar al siguiente número no marcado
        5. Repetir hasta √n

        **Complejidad:** O(n log log n)

        Fue inventado por Eratóstenes de Cirene alrededor del 200 a.C.
        """)

    st.markdown("---")

    # Controles
    col1, col2 = st.columns([3, 1])
    with col1:
        limite_criba = st.slider("Límite para la criba:", 10, 200, 50, 5)
    with col2:
        st.write("")
        st.write("")
        ejecutar = st.button("▶️ Ejecutar Criba", use_container_width=True, type="primary")

    if ejecutar:
        with st.spinner("Ejecutando Criba de Eratóstenes..."):
            pasos = criba_eratostenes_pasos(limite_criba)

            if pasos:
                st.success(f"Criba completada. Se encontraron primos hasta {limite_criba}.")

                # Mostrar visualización final
                estado_final = pasos[-1]["estado"]
                primos_encontrados = [i for i, es_primo in enumerate(estado_final) if es_primo]

                st.write(f"**Números primos encontrados ({len(primos_encontrados)}):**")
                st.write(", ".join(map(str, primos_encontrados[:50])))
                if len(primos_encontrados) > 50:
                    st.write(f"... y {len(primos_encontrados) - 50} más")

                # Visualización con heatmap
                if limite_criba <= 100:
                    dimension = 10
                    fig = heatmap_criba(estado_final, dimension)
                    st.plotly_chart(fig, use_container_width=True)

                # Mostrar algunos pasos
                if st.checkbox("Ver pasos detallados"):
                    for i, paso in enumerate(pasos[:10]):  # Primeros 10 pasos
                        if paso["accion"] == "marcar_multiplos":
                            st.write(f"**Paso {i+1}:** Marcando múltiplos de {paso['numero_actual']}")
                            st.write(f"Marcados: {paso['marcados'][:10]}{'...' if len(paso['marcados']) > 10 else ''}")


# ==================== TAB 4: HERRAMIENTAS ====================

def tab_herramientas():
    """Tab de herramientas matemáticas"""
    st.header("🧰 Herramientas Matemáticas")

    herramienta = st.selectbox(
        "Selecciona una herramienta:",
        ["Generador de Primos en Rango", "Factorización Prima",
         "Tabla de Primeros N Primos", "Buscar N-ésimo Primo", "Primos Gemelos"]
    )

    st.markdown("---")

    if herramienta == "Generador de Primos en Rango":
        st.subheader("Generar Primos en un Rango")

        col1, col2 = st.columns(2)
        with col1:
            inicio = st.number_input("Inicio del rango:", 0, 100000, 10)
        with col2:
            fin = st.number_input("Fin del rango:", inicio, 100000, 100)

        if st.button("Generar"):
            with st.spinner("Buscando primos..."):
                primos = primos_en_rango(inicio, fin)
                st.success(f"Se encontraron **{len(primos)}** primos entre {inicio} y {fin}.")

                if primos:
                    st.write(", ".join(map(str, primos[:100])))
                    if len(primos) > 100:
                        st.write(f"... y {len(primos) - 100} más")

                    # Opción de descarga
                    df = pd.DataFrame({"Primos": primos})
                    csv = df.to_csv(index=False)
                    st.download_button(
                        "📥 Descargar como CSV",
                        csv,
                        "primos.csv",
                        "text/csv"
                    )

    elif herramienta == "Factorización Prima":
        st.subheader("Calculadora de Factorización Prima")

        numero = st.number_input("Número a factorizar:", 2, 1000000, 60)

        if st.button("Factorizar"):
            factores = factorizacion_prima(numero)

            if factores:
                expresion = " × ".join([
                    f"{f}^{e}" if e > 1 else f"{f}"
                    for f, e in sorted(factores.items())
                ])
                st.success(f"**{numero} = {expresion}**")

                # Tabla de factores
                df = pd.DataFrame({
                    "Factor Primo": list(factores.keys()),
                    "Exponente": list(factores.values())
                })
                st.dataframe(df, use_container_width=True)

                # Visualización
                fig = visualizar_factorizacion(numero, factores)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)

    elif herramienta == "Tabla de Primeros N Primos":
        st.subheader("Tabla de Primeros N Números Primos")

        n = st.number_input("¿Cuántos primos quieres generar?", 1, 1000, 50)

        if st.button("Generar Tabla"):
            with st.spinner("Generando primos..."):
                # Estimar límite
                if n < 10:
                    limite = 30
                else:
                    import math
                    limite = int(n * (math.log(n) + math.log(math.log(n)) + 2))

                primos = calcular_primos_cached(limite)
                primeros_n = primos[:n]

                st.success(f"Primeros {n} números primos generados.")

                # Crear tabla
                df = pd.DataFrame({
                    "Posición": range(1, len(primeros_n) + 1),
                    "Primo": primeros_n
                })

                st.dataframe(df, use_container_width=True, height=400)

    elif herramienta == "Buscar N-ésimo Primo":
        st.subheader("Encontrar el N-ésimo Número Primo")

        n = st.number_input("Posición del primo (n):", 1, 10000, 10)

        if st.button("Buscar"):
            with st.spinner("Buscando..."):
                primo = enesimo_primo(n)
                st.success(f"El primo número **{n}** es **{primo}**")

                st.info(f"Por ejemplo: el 1er primo es 2, el 10mo primo es 29, el 100vo primo es 541.")

    elif herramienta == "Primos Gemelos":
        st.subheader("Encontrar Pares de Primos Gemelos")

        st.info("Los primos gemelos son pares de primos que difieren en 2, como (3,5), (11,13), (17,19).")

        limite = st.number_input("Buscar hasta:", 10, 10000, 100)

        if st.button("Buscar Gemelos"):
            with st.spinner("Buscando primos gemelos..."):
                gemelos = primos_gemelos(limite)

                st.success(f"Se encontraron **{len(gemelos)}** pares de primos gemelos hasta {limite}.")

                if gemelos:
                    # Mostrar en tabla
                    df = pd.DataFrame(gemelos, columns=["Primo 1", "Primo 2"])
                    st.dataframe(df, use_container_width=True, height=400)


# ==================== TAB 5: TEORÍA ====================

def tab_teoria():
    """Tab de teoría y educación"""
    st.header("📚 Teoría y Educación")

    seccion = st.selectbox(
        "Selecciona un tema:",
        ["Conceptos Básicos", "Historia de los Primos", "Aplicaciones Reales",
         "Teoremas Importantes", "Algoritmos de Verificación", "Curiosidades"]
    )

    st.markdown("---")

    if seccion == "Conceptos Básicos":
        st.markdown(obtener_teoria_basica())

    elif seccion == "Historia de los Primos":
        st.markdown(obtener_historia_primos())

    elif seccion == "Aplicaciones Reales":
        st.markdown(obtener_aplicaciones_reales())

    elif seccion == "Teoremas Importantes":
        st.markdown(obtener_teoremas_importantes())

    elif seccion == "Algoritmos de Verificación":
        st.markdown(comparacion_algoritmos())

    elif seccion == "Curiosidades":
        st.markdown(obtener_curiosidades())


# ==================== TAB 6: GAMIFICACIÓN ====================

def tab_gamificacion():
    """Tab de gamificación y quiz"""
    st.header("🎮 Quiz y Retos sobre Números Primos")

    # Selector de nivel
    nivel = st.radio(
        "Selecciona el nivel de dificultad:",
        ["facil", "medio", "dificil"],
        format_func=lambda x: {"facil": "😊 Fácil", "medio": "🤔 Medio", "dificil": "🧠 Difícil"}[x],
        horizontal=True
    )

    st.markdown("---")

    # Generar nueva pregunta o mostrar la actual
    if st.button("🎲 Nueva Pregunta") or st.session_state.pregunta_actual is None:
        st.session_state.pregunta_actual = generar_pregunta_quiz(nivel)
        st.session_state.tiempo_pregunta = time.time()
        st.rerun()

    pregunta = st.session_state.pregunta_actual

    # Mostrar pregunta
    st.subheader(pregunta["pregunta"])

    # Opciones de respuesta
    respuesta = st.radio(
        "Selecciona tu respuesta:",
        pregunta["opciones"],
        key=f"respuesta_{id(pregunta)}"
    )

    # Botón de verificar
    if st.button("✅ Verificar Respuesta", type="primary"):
        tiempo_usado = time.time() - st.session_state.tiempo_pregunta
        es_correcta, explicacion = verificar_respuesta(pregunta, respuesta)

        if es_correcta:
            puntos = calcular_puntuacion(tiempo_usado, nivel, True)
            st.session_state.puntuacion_quiz += puntos
            st.session_state.respuestas_correctas += 1

            st.success(f"🎉 ¡Correcto! +{puntos} puntos")
            st.balloons()
        else:
            st.session_state.respuestas_incorrectas += 1
            st.error("❌ Incorrecto")

        st.info(f"**Explicación:** {explicacion}")

        # Mostrar tiempo
        st.write(f"⏱️ Tiempo: {tiempo_usado:.1f} segundos")

    # Estadísticas del quiz
    st.markdown("---")
    st.subheader("📊 Estadísticas del Quiz")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Puntuación Total", st.session_state.puntuacion_quiz)
    with col2:
        st.metric("Correctas", st.session_state.respuestas_correctas, delta_color="normal")
    with col3:
        st.metric("Incorrectas", st.session_state.respuestas_incorrectas, delta_color="inverse")

    # Título actual
    titulo, icono = obtener_titulo_usuario(st.session_state.puntuacion_quiz)
    st.success(f"{icono} **Rango actual:** {titulo}")


# ==================== TAB 7: ESTADÍSTICAS ====================

def tab_estadisticas():
    """Tab de estadísticas de uso"""
    st.header("📈 Estadísticas de Uso")

    # Resumen general
    st.subheader("Resumen de Actividad")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Verificaciones", st.session_state.verificaciones)
    with col2:
        st.metric("Puntos Quiz", st.session_state.puntuacion_quiz)
    with col3:
        correctas = st.session_state.respuestas_correctas
        incorrectas = st.session_state.respuestas_incorrectas
        total_quiz = correctas + incorrectas
        tasa = (correctas / total_quiz * 100) if total_quiz > 0 else 0
        st.metric("Tasa Aciertos", f"{tasa:.1f}%")
    with col4:
        st.metric("Mayor Primo", st.session_state.primo_mas_grande_encontrado)

    st.markdown("---")

    # Historial de verificaciones
    if st.session_state.historial:
        st.subheader("📊 Números Más Verificados")

        fig = grafico_estadisticas_sesion(st.session_state.historial)
        if fig:
            st.plotly_chart(fig, use_container_width=True)

        # Tabla de historial reciente
        if st.checkbox("Ver historial completo"):
            df_historial = pd.DataFrame({
                "Verificación": range(1, len(st.session_state.historial) + 1),
                "Número": st.session_state.historial
            })
            st.dataframe(df_historial.iloc[::-1], use_container_width=True, height=300)

    else:
        st.info("Todavía no has verificado ningún número. ¡Ve al Verificador para comenzar!")

    st.markdown("---")

    # Logros desbloqueados
    st.subheader("🏆 Logros Desbloqueados")

    estadisticas = {
        "verificaciones": st.session_state.verificaciones,
        "puntuacion_quiz": st.session_state.puntuacion_quiz,
        "primo_mas_grande_encontrado": st.session_state.primo_mas_grande_encontrado
    }
    logros = verificar_logros(estadisticas)

    if logros:
        cols = st.columns(3)
        for i, logro in enumerate(logros):
            with cols[i % 3]:
                st.success(f"{logro['icono']} **{logro['nombre']}**\n\n{logro['descripcion']}")
    else:
        st.info("¡Aún no has desbloqueado ningún logro! Sigue explorando.")


# ==================== MAIN ====================

def main():
    """Función principal de la aplicación"""
    # Inicialización
    load_custom_css()
    init_session_state()

    # Header
    st.markdown('<div class="main-header"><h1>🔢 Academia Interactiva de Números Primos</h1><p>Explora, aprende y domina la teoría de números primos</p></div>', unsafe_allow_html=True)

    # Sidebar
    render_sidebar()

    # Crear tabs
    tabs = st.tabs([
        "🏠 Verificador",
        "📊 Visualizaciones",
        "🎨 Criba de Eratóstenes",
        "🧰 Herramientas",
        "📚 Teoría",
        "🎮 Quiz",
        "📈 Estadísticas"
    ])

    with tabs[0]:
        tab_verificador()

    with tabs[1]:
        tab_visualizaciones()

    with tabs[2]:
        tab_criba()

    with tabs[3]:
        tab_herramientas()

    with tabs[4]:
        tab_teoria()

    with tabs[5]:
        tab_gamificacion()

    with tabs[6]:
        tab_estadisticas()

    # Footer
    st.markdown("---")
    st.markdown(
        '<div style="text-align: center; color: #666; padding: 20px;">'
        'Desarrollado con ❤️ usando Streamlit | '
        '© 2024 Academia de Números Primos'
        '</div>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()

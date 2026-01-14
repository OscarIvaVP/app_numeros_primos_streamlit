# 🔢 Academia Interactiva de Números Primos

[![Streamlit](https://img.shields.io/badge/Streamlit-1.40.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.24.1-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

> Una aplicación web educativa completa e interactiva para explorar, aprender y dominar la teoría de números primos.

## 📖 Descripción

**Academia Interactiva de Números Primos** es una plataforma educativa desarrollada con Streamlit que transforma el aprendizaje de la teoría de números primos en una experiencia visual, interactiva y gamificada. Diseñada para estudiantes de bachillerato y universidad inicial, la aplicación combina rigor matemático con una interfaz intuitiva y atractiva.

### ✨ Características Principales

- 🔍 **Verificador de Primalidad Avanzado** - Comprueba si un número es primo con análisis detallado y factorización visual
- 📊 **Visualizaciones Interactivas** - 8 tipos de gráficos incluyendo la famosa Espiral de Ulam
- 🎨 **Criba de Eratóstenes Animada** - Observa el algoritmo antiguo en acción paso a paso
- 🧰 **Suite de Herramientas Matemáticas** - Generadores, calculadoras y buscadores especializados
- 📚 **Contenido Educativo Extenso** - Teoría, historia, aplicaciones y teoremas importantes
- 🎮 **Gamificación Completa** - Quiz multinivel, sistema de puntuación y logros desbloqueables
- 📈 **Estadísticas de Uso** - Seguimiento de actividad, historial y métricas personales

---

## 🚀 Demo en Vivo

🌐 **[Ver Aplicación en Streamlit Cloud]**(https://appnumerosprimos.streamlit.app/)

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.9+ | Lenguaje de programación |
| **Streamlit** | 1.40.0 | Framework web interactivo |
| **Plotly** | 5.24.1 | Visualizaciones interactivas |
| **Matplotlib** | 3.9.3 | Gráficos estáticos y heatmaps |
| **NumPy** | 1.26.4 | Computación científica |
| **Pandas** | 2.2.3 | Manipulación de datos |

---

## 📁 Estructura del Proyecto

```
app_numeros_primos_streamlit/
│
├── app.py                      # Aplicación principal (725 líneas)
├── requirements.txt            # Dependencias del proyecto
├── README.md                   # Documentación (este archivo)
│
└── utils/                      # Módulos auxiliares
    ├── __init__.py
    ├── prime_algorithms.py     # Algoritmos de números primos (~450 líneas)
    ├── visualizations.py       # Funciones de visualización (~300 líneas)
    ├── gamification.py         # Sistema de quiz y logros (~250 líneas)
    └── educational_content.py  # Contenido educativo (~400 líneas)
```

### Descripción de Módulos

**`utils/prime_algorithms.py`**
- Verificación de primalidad (básico, con pasos, Miller-Rabin)
- Generación de primos (Criba de Eratóstenes, rangos, n-ésimo primo)
- Factorización prima
- Análisis de propiedades (primos gemelos, distancia a primo más cercano)

**`utils/visualizations.py`**
- Gráficos de distribución de primos
- Función π(x) vs aproximación x/ln(x)
- Espiral de Ulam
- Heatmaps de la Criba de Eratóstenes
- Análisis de brechas entre primos
- Visualización de factorización

**`utils/gamification.py`**
- Preguntas de quiz (fácil, medio, difícil)
- Sistema de puntuación con bonos por velocidad
- Verificación de logros
- Sistema de rangos (Aprendiz → Gran Maestro)

**`utils/educational_content.py`**
- Teoría básica de números primos
- Historia desde Euclides hasta la actualidad
- Aplicaciones en criptografía (RSA)
- Teoremas importantes (TFA, infinitud de primos, Riemann)
- Comparación de algoritmos
- Curiosidades matemáticas

---

## 💻 Instalación Local

### Prerrequisitos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/TU_USUARIO/app_numeros_primos_streamlit.git
cd app_numeros_primos_streamlit
```

2. **Crear un entorno virtual (recomendado)**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

---

## 📱 Uso de la Aplicación

### Navegación

La aplicación está organizada en **7 pestañas principales** accesibles desde la parte superior:

---

### 1. 🏠 Verificador de Números Primos

**Funcionalidades:**
- Verificación instantánea de primalidad con tiempo de ejecución
- Factorización prima completa para números compuestos
- Visualización gráfica de la factorización
- Análisis del primo más cercano
- Detección automática de pares gemelos

**Ejemplo de uso:**
1. Ingresa un número (ej: 60)
2. Click en "🔍 Verificar"
3. Observa que 60 = 2² × 3 × 5
4. Visualiza el gráfico de factorización

---

### 2. 📊 Visualizaciones Interactivas

**Tipos de visualizaciones:**

**Distribución de Primos**
- Histograma que muestra cómo se distribuyen los primos hasta un límite
- Ajusta el límite con el slider (10 - 10,000)

**Función π(x)**
- Compara la cantidad real de primos con la aproximación x/ln(x)
- Demuestra visualmente el Teorema de los Números Primos

**Espiral de Ulam**
- Patrón visual sorprendente descubierto por Stanislaw Ulam en 1963
- Los números primos forman diagonales misteriosas
- Ajusta la dimensión (11×11 hasta 101×101)

**Comparación Primos vs Compuestos**
- Gráfico de barras comparativo
- Muestra la proporción de primos en un rango

**Brechas entre Primos**
- Scatter plot de las distancias entre primos consecutivos
- Visualiza la irregularidad en la distribución

---

### 3. 🎨 Criba de Eratóstenes

**Características:**
- Explicación teórica del algoritmo (200 a.C.)
- Ejecución paso a paso del algoritmo
- Visualización con heatmap (verde = primo, rojo = compuesto)
- Detalles de cada paso de marcado

**Cómo usar:**
1. Ajusta el límite (10 - 200)
2. Click en "▶️ Ejecutar Criba"
3. Observa los resultados y la visualización
4. Marca "Ver pasos detallados" para análisis profundo

---

### 4. 🧰 Herramientas Matemáticas

**5 herramientas especializadas:**

**Generador de Primos en Rango**
- Encuentra todos los primos entre dos números
- Descarga resultados en formato CSV
- Ejemplo: Primos entre 100 y 200

**Factorización Prima**
- Descompone cualquier número en sus factores primos
- Muestra tabla de factores y exponentes
- Gráfico visual de contribución de cada factor

**Tabla de Primeros N Primos**
- Genera lista de los primeros N números primos
- Tabla interactiva con posición y valor
- Hasta 1,000 primos

**Buscar N-ésimo Primo**
- Encuentra el primo en la posición N
- Ejemplo: El 100º primo es 541

**Primos Gemelos**
- Encuentra pares de primos que difieren en 2
- Ejemplos: (3,5), (11,13), (17,19)
- Tabla completa de resultados

---

### 5. 📚 Teoría y Educación

**6 secciones educativas:**

**Conceptos Básicos**
- Definición formal de número primo
- Propiedades fundamentales
- Casos especiales (1, 2, números pares)

**Historia de los Primos**
- Desde Euclides (300 a.C.) hasta la era computacional
- Grandes matemáticos: Fermat, Euler, Riemann
- Récords actuales (primos de Mersenne)

**Aplicaciones Reales**
- Criptografía RSA (HTTPS, firmas digitales)
- Algoritmos de hashing
- Ciencias naturales (cicadas)
- Teoría de códigos

**Teoremas Importantes**
- Teorema Fundamental de la Aritmética
- Infinitud de los Primos (demostración de Euclides)
- Teorema de los Números Primos
- Pequeño Teorema de Fermat
- Conjetura de los Primos Gemelos
- Hipótesis de Riemann

**Algoritmos de Verificación**
- Comparación: División por Prueba, Criba, Fermat, Miller-Rabin, AKS
- Complejidades temporales
- Ventajas y desventajas de cada método
- Tabla comparativa de rendimiento

**Curiosidades**
- Mayor primo conocido (24+ millones de dígitos)
- Primos palíndromos
- Espiral de Ulam
- Récords y premios
- Números primos en la cultura popular

---

### 6. 🎮 Quiz y Gamificación

**Sistema de quiz interactivo:**

**3 Niveles de Dificultad:**
- 😊 **Fácil:** Conceptos básicos (¿Es 2 primo? ¿Cuántos primos hay <10?)
- 🤔 **Medio:** Primos gemelos, Criba de Eratóstenes, conteo de primos
- 🧠 **Difícil:** Teoremas, algoritmos, complejidades, historia

**Sistema de Puntuación:**
- Puntos base según dificultad (10/20/30)
- Bonus por velocidad (hasta +10 puntos)
- Acumulación de puntos para subir de rango

**Rangos del Usuario:**
- 🌱 Aprendiz (0-49 pts)
- 📖 Estudiante (50-149 pts)
- 🔢 Matemático (150-299 pts)
- ⭐ Experto (300-499 pts)
- 🏆 Gran Maestro (500+ pts)

**Características:**
- Explicaciones inmediatas tras cada respuesta
- Timer automático para cálculo de bonos
- Estadísticas de aciertos/fallos
- Feedback visual (confeti en respuestas correctas)

---

### 7. 📈 Estadísticas de Uso

**Métricas de Actividad:**
- Total de verificaciones realizadas
- Puntuación acumulada en quiz
- Tasa de aciertos (%)
- Mayor número primo verificado

**Visualizaciones:**
- Gráfico de números más verificados (Top 10)
- Historial completo de verificaciones

**Sistema de Logros:**

| Logro | Requisito | Icono |
|-------|-----------|-------|
| Explorador de Primos | 10 verificaciones | 🔍 |
| Cazador de Primos | 50 verificaciones | 🎯 |
| Maestro de Primos | 100 verificaciones | 👑 |
| Estudiante Aplicado | 50 puntos en quiz | 📚 |
| Erudito Matemático | 200 puntos en quiz | 🎓 |
| Buscador de Gigantes | Verificar número >1000 | 🗿 |

---

## 🌐 Despliegue en Streamlit Cloud

### Pasos para Desplegar

1. **Preparar el repositorio**
   - Asegúrate de que todos los archivos estén en GitHub
   - Verifica que `requirements.txt` esté actualizado

2. **Subir cambios a GitHub**
```bash
git add .
git commit -m "Aplicación completa de números primos"
git push origin main
```

3. **Conectar con Streamlit Cloud**
   - Ve a [share.streamlit.io](https://share.streamlit.io/)
   - Inicia sesión con tu cuenta de GitHub
   - Click en "New app"

4. **Configurar el despliegue**
   - **Repository:** `app_numeros_primos_streamlit`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **Python version:** 3.11 (recomendado)

5. **Deploy**
   - Click en "Deploy!"
   - Espera 2-3 minutos
   - Tu app estará en: `https://[usuario]-app-numeros-primos-streamlit.streamlit.app`

---

## 🎯 Casos de Uso Educativo

### Para Estudiantes

- **Autoaprendizaje:** Explora conceptos a tu propio ritmo
- **Práctica:** Quiz interactivo con retroalimentación inmediata
- **Visualización:** Entiende patrones abstractos con gráficos
- **Experimentación:** Prueba diferentes números y observa resultados

### Para Profesores

- **Herramienta de Enseñanza:** Demostraciones en clase
- **Tareas Interactivas:** Asigna exploración de temas específicos
- **Evaluación:** Usa el quiz para revisar comprensión
- **Recursos:** Contenido teórico completo como referencia

### Para Entusiastas de las Matemáticas

- **Exploración Avanzada:** Primos gemelos, Espiral de Ulam
- **Verificación Rápida:** Herramientas para investigación personal
- **Aprendizaje Continuo:** Curiosidades y teoremas avanzados

---

## 📊 Métricas del Proyecto

| Métrica | Valor |
|---------|-------|
| **Líneas de código** | ~1,625 |
| **Funciones implementadas** | 40+ |
| **Visualizaciones** | 8 tipos |
| **Preguntas de quiz** | 20+ |
| **Secciones educativas** | 6 |
| **Herramientas** | 5 |
| **Logros desbloqueables** | 6 |

---

## 🔬 Algoritmos Implementados

### Verificación de Primalidad

1. **División por Prueba Optimizada**
   - Complejidad: O(√n)
   - Solo verifica divisores de forma 6k ± 1
   - Ideal para n < 10⁶

2. **Test de Miller-Rabin**
   - Complejidad: O(k log³ n)
   - Probabilístico
   - Para números grandes (n > 10⁶)

### Generación de Primos

1. **Criba de Eratóstenes**
   - Complejidad: O(n log log n)
   - Genera todos los primos hasta n
   - Optimizado con memoria

2. **Búsqueda del N-ésimo Primo**
   - Usa aproximación π(x) ≈ x/ln(x)
   - Ajuste dinámico del límite

### Análisis

1. **Factorización Prima**
   - Descomposición completa en factores
   - Formato: {factor: exponente}

2. **Propiedades**
   - Función π(x): conteo de primos
   - Primos gemelos: pares que difieren en 2
   - Distancia a primo más cercano

---

## 🚧 Roadmap Futuro

### Versión 2.0 (Planificada)

- [ ] Algoritmo AKS (test determinista polinomial)
- [ ] Generador de primos de Mersenne
- [ ] Espiral de Sacks (alternativa a Ulam)
- [ ] Exportación de gráficos como PNG/PDF
- [ ] Sistema de usuarios con login
- [ ] Leaderboard global
- [ ] Modo oscuro (dark theme)
- [ ] Soporte multilenguaje (inglés/español)
- [ ] API REST para consultas programáticas
- [ ] Desafíos diarios automatizados

### Mejoras en Consideración

- Animaciones más fluidas en la Criba
- Cálculo de primos en Web Workers (para no bloquear UI)
- Caché persistente entre sesiones
- Tutorial interactivo para nuevos usuarios
- Sección de "Desafíos de la Comunidad"

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar esta aplicación:

1. **Fork** el repositorio
2. Crea una **rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add: Amazing Feature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. Abre un **Pull Request**

### Áreas donde puedes contribuir

- 🐛 Reportar bugs
- 💡 Sugerir nuevas características
- 📝 Mejorar documentación
- 🎨 Diseño y UX
- 🔬 Nuevos algoritmos
- 🌐 Traducciones

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

```
MIT License

Copyright (c) 2024 [Tu Nombre]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👨‍💻 Autor

**Miguel Rico**

- GitHub: [@TU_USUARIO](https://github.com/TU_USUARIO)
- LinkedIn: [Tu Perfil](https://linkedin.com/in/tu-perfil)

---

## 🙏 Agradecimientos

- **Streamlit Team** por el increíble framework
- **Plotly** por las visualizaciones interactivas
- **Euclides** por demostrar la infinitud de los primos
- **Eratóstenes** por su algoritmo milenario
- **Todos los matemáticos** que han contribuido a la teoría de números

---

## 📚 Referencias

### Teoría de Números Primos
- Hardy, G. H., & Wright, E. M. (2008). *An Introduction to the Theory of Numbers*
- Ribenboim, P. (1995). *The New Book of Prime Number Records*

### Algoritmos
- Knuth, D. E. (1997). *The Art of Computer Programming, Vol. 2: Seminumerical Algorithms*
- Agrawal, M., Kayal, N., & Saxena, N. (2004). *PRIMES is in P*

### Recursos Online
- [OEIS - Secuencia A000040 (Números Primos)](https://oeis.org/A000040)
- [GIMPS - Great Internet Mersenne Prime Search](https://www.mersenne.org/)
- [Prime Pages - The Prime Glossary](https://t5k.org/glossary/)

---

## 💬 Contacto y Soporte

¿Tienes preguntas o sugerencias?

- 📧 Email: tu.email@ejemplo.com
- 💬 Issues: [GitHub Issues](https://github.com/TU_USUARIO/app_numeros_primos_streamlit/issues)
- 🐦 Twitter: [@TuUsuario](https://twitter.com/TuUsuario)

---

<div align="center">

**⭐ Si te gusta este proyecto, dale una estrella en GitHub ⭐**

Desarrollado con ❤️ y Python

</div>

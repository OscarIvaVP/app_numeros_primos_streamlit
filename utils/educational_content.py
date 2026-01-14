# -*- coding: utf-8 -*-
"""
Módulo de contenido educativo sobre números primos
Contiene explicaciones teóricas, historia, aplicaciones y más
"""


def obtener_teoria_basica() -> str:
    """
    Retorna contenido markdown con la teoría básica de números primos.
    """
    return """
## ¿Qué es un número primo?

Un **número primo** es un número natural mayor que 1 que tiene únicamente dos divisores distintos: **1 y él mismo**.

### Definición Formal

Un número entero positivo \( p > 1 \) es primo si y solo si:
- Sus únicos divisores positivos son 1 y \( p \)
- No puede expresarse como producto de dos números naturales menores que él

### Ejemplos

**Números primos:** 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31...

**Números NO primos (compuestos):**
- 4 = 2 × 2
- 6 = 2 × 3
- 9 = 3 × 3
- 15 = 3 × 5

### Casos Especiales

- **1** NO es primo (por definición, necesita exactamente dos divisores)
- **2** es el único número primo par
- Todos los demás números primos son impares

### Propiedades Fundamentales

1. **Infinitud:** Existen infinitos números primos (demostrado por Euclides ~300 a.C.)
2. **Distribución:** Los primos se vuelven menos frecuentes a medida que los números crecen
3. **Importancia:** Son los "bloques de construcción" de todos los números naturales
"""


def obtener_historia_primos() -> str:
    """
    Retorna contenido markdown sobre la historia de los números primos.
    """
    return """
## Historia de los Números Primos

### Antigüedad

**~300 a.C. - Euclides (Grecia)**
- Demostró que existen infinitos números primos
- Desarrolló el algoritmo de Euclides para el máximo común divisor
- Su demostración es considerada una de las más elegantes de la matemática

**~200 a.C. - Eratóstenes de Cirene**
- Inventó la **Criba de Eratóstenes**, método para encontrar todos los primos hasta un límite
- Algoritmo aún utilizado en la actualidad

### Era Moderna

**Siglo XVII - Pierre de Fermat**
- Propuso varios teoremas sobre números primos
- Números de Fermat: \( F_n = 2^{2^n} + 1 \)

**Siglo XVIII - Leonhard Euler**
- Extendió el trabajo de Fermat
- Desarrolló la función φ de Euler (función totiente)

**1859 - Bernhard Riemann**
- Propuso la **Hipótesis de Riemann**, problema del milenio sin resolver
- Relaciona la distribución de primos con los ceros de la función zeta

### Era Computacional

**1951 - Primera búsqueda computacional**
- EDSAC encuentra primos de forma automatizada

**1970s - Desarrollo de RSA**
- Uso de números primos en criptografía de clave pública
- Revolucionó la seguridad informática

**2018 - Último récord**
- Mayor primo conocido: \( 2^{82,589,933} - 1 \) (primo de Mersenne)
- Tiene 24,862,048 dígitos
"""


def obtener_aplicaciones_reales() -> str:
    """
    Retorna contenido markdown sobre aplicaciones de números primos.
    """
    return """
## Aplicaciones de los Números Primos

### 1. Criptografía (Uso Principal)

**RSA (Rivest-Shamir-Adleman)**
- Sistema criptográfico de clave pública más utilizado
- Se basa en la dificultad de factorizar números muy grandes
- Funciona así:
  1. Se eligen dos primos grandes \( p \) y \( q \) (cientos de dígitos)
  2. Se calcula \( n = p × q \)
  3. Es fácil multiplicar, pero muy difícil factorizar \( n \) de vuelta a \( p \) y \( q \)

**Aplicaciones de RSA:**
- HTTPS (navegación web segura)
- Firmas digitales
- Criptomonedas
- Comunicaciones bancarias

### 2. Algoritmos de Hashing

- Uso de números primos en funciones hash
- Tablas hash utilizan tamaños primos para minimizar colisiones
- Algoritmos de dispersión en bases de datos

### 3. Generadores de Números Pseudoaleatorios

- Números primos en algoritmos PRNG
- Generación de secuencias con buen período
- Simulaciones Monte Carlo

### 4. Ciencias Naturales

**Cicadas (Cigarras)**
- Magicicada septendecim: ciclo de vida de 13 o 17 años (ambos primos)
- Estrategia evolutiva para evitar depredadores con ciclos predecibles

### 5. Música y Arte

- Ritmos basados en números primos
- Estructuras arquitectónicas y diseño
- Patrones visuales (espiral de Ulam)

### 6. Teoría de Códigos

- Códigos de corrección de errores
- Compresión de datos
- Códigos BCH (Bose-Chaudhuri-Hocquenghem)
"""


def obtener_teoremas_importantes() -> str:
    """
    Retorna contenido markdown sobre teoremas importantes relacionados con primos.
    """
    return """
## Teoremas Importantes sobre Números Primos

### 1. Teorema Fundamental de la Aritmética

**Enunciado:**
> Todo número natural mayor que 1 puede expresarse de manera única como producto de números primos (salvo el orden).

**Ejemplo:**
- 60 = 2² × 3 × 5
- 100 = 2² × 5²
- 315 = 3² × 5 × 7

**Importancia:** Los primos son los "átomos" de los números naturales.

---

### 2. Infinitud de los Primos (Euclides)

**Enunciado:**
> Existen infinitos números primos.

**Demostración (por contradicción):**
1. Supongamos que hay un número finito de primos: \( p_1, p_2, ..., p_n \)
2. Consideremos \( N = (p_1 × p_2 × ... × p_n) + 1 \)
3. \( N \) no es divisible por ninguno de los primos conocidos
4. Por tanto, \( N \) es primo o tiene un factor primo nuevo
5. Contradicción → hay infinitos primos

---

### 3. Teorema de los Números Primos

**Enunciado:**
> La función \( π(x) \) que cuenta los primos menores o iguales a \( x \) se aproxima a:

\[ π(x) ≈ \\frac{x}{\\ln(x)} \]

**Consecuencia:**
- La probabilidad de que un número \( n \) sea primo es aproximadamente \( 1/\\ln(n) \)
- Los primos se hacen más escasos a medida que los números crecen

---

### 4. Teorema de Fermat (Pequeño)

**Enunciado:**
> Si \( p \) es primo y \( a \) no es divisible por \( p \), entonces:

\[ a^{p-1} ≡ 1 \\ (\\text{mod} \\ p) \]

**Aplicación:** Base de tests de primalidad probabilísticos.

---

### 5. Conjetura de los Primos Gemelos (No demostrada)

**Enunciado:**
> Existen infinitos pares de primos que difieren en 2.

**Ejemplos:** (3,5), (5,7), (11,13), (17,19), (29,31)...

**Estado:** Problema abierto desde hace siglos.

---

### 6. Hipótesis de Riemann (No demostrada)

**Enunciado:**
> Todos los ceros no triviales de la función zeta de Riemann tienen parte real \( 1/2 \).

**Importancia:**
- Problema del milenio ($1,000,000 de premio)
- Implicaría resultados profundos sobre la distribución de primos

---

### 7. Teorema de Dirichlet

**Enunciado:**
> Si \( a \) y \( b \) son coprimos, existen infinitos primos de la forma \( a + nb \).

**Ejemplo:** Infinitos primos terminan en 1, 3, 7 o 9 (base 10).
"""


def comparacion_algoritmos() -> str:
    """
    Retorna contenido markdown con comparación de algoritmos de primalidad.
    """
    return """
## Algoritmos de Verificación de Primalidad

### 1. División por Prueba (Trial Division)

**Método:** Dividir por todos los números desde 2 hasta √n

**Complejidad:** O(√n)

**Ventajas:**
- Simple de implementar
- Determinista (100% preciso)
- Funciona bien para números pequeños (<10⁶)

**Desventajas:**
- Muy lento para números grandes
- No práctico para n > 10¹²

---

### 2. Criba de Eratóstenes

**Método:** Marcar múltiplos de cada primo encontrado

**Complejidad:** O(n log log n)

**Ventajas:**
- Muy eficiente para encontrar TODOS los primos hasta n
- Simple de implementar
- Excelente para rangos

**Desventajas:**
- Requiere mucha memoria: O(n)
- No sirve para verificar UN número grande específico

---

### 3. Test de Fermat

**Método:** Verificar si \( a^{n-1} ≡ 1 \\ (\\text{mod} \\ n) \) para varios valores de \( a \)

**Complejidad:** O(k log n) donde k = número de pruebas

**Ventajas:**
- Mucho más rápido que división por prueba
- Probabilístico: puede ajustarse la confianza

**Desventajas:**
- Falsos positivos: números de Carmichael
- No 100% confiable

---

### 4. Test de Miller-Rabin

**Método:** Mejora del test de Fermat, evita números de Carmichael

**Complejidad:** O(k log³ n)

**Ventajas:**
- Muy rápido para números grandes
- Probabilidad de error < \( 4^{-k} \)
- Usado en práctica para criptografía

**Desventajas:**
- Probabilístico (no determinista)
- Más complejo de implementar

---

### 5. Test AKS (2002)

**Método:** Primer algoritmo determinista y polinomial

**Complejidad:** O(log⁶ n) (mejorado a O(log⁴ n))

**Ventajas:**
- Determinista (100% preciso)
- Complejidad polinomial

**Desventajas:**
- Constantes muy grandes
- En la práctica, más lento que Miller-Rabin
- Principalmente de interés teórico

---

## Comparación Práctica

| Algoritmo | n < 10⁶ | 10⁶ < n < 10¹² | n > 10¹² | Determinista |
|-----------|---------|----------------|----------|--------------|
| División por Prueba | ✓✓✓ | ✗ | ✗ | Sí |
| Criba Eratóstenes | ✓✓✓ | ✗ | ✗ | Sí |
| Fermat | ✓✓ | ✓✓ | ✓ | No |
| Miller-Rabin | ✓✓ | ✓✓✓ | ✓✓✓ | No |
| AKS | ✓ | ✓ | ✓ | Sí |

**Recomendación:**
- n < 10⁶: División por prueba o Criba
- n > 10⁶: Miller-Rabin con k=5-10 rondas
"""


def obtener_curiosidades() -> str:
    """
    Retorna contenido markdown con curiosidades sobre números primos.
    """
    return """
## Curiosidades sobre Números Primos

### Récords y Números Especiales

**Mayor primo conocido (2024)**
- \( 2^{82,589,933} - 1 \)
- Tiene 24,862,048 dígitos
- Es un **primo de Mersenne** (forma \( 2^p - 1 \))
- Descubierto por GIMPS (Great Internet Mersenne Prime Search)

**Primos Palíndromos**
- Números primos que se leen igual al revés
- Ejemplos: 11, 101, 131, 151, 181, 191, 313, 353...
- ¿Existen infinitos? No se sabe.

**Primos de Sophie Germain**
- Un primo \( p \) tal que \( 2p + 1 \) también es primo
- Ejemplos: 2, 3, 5, 11, 23, 29, 41, 53...
- Nombrados por Sophie Germain (matemática francesa, 1776-1831)

### Patrones Curiosos

**23 consecutivos compuestos**
- Entre 89 y 97 no hay primos
- Existen "desiertos de primos" arbitrariamente grandes

**Constante de Brun**
- Suma de los inversos de primos gemelos: \( ≈ 1.902 \)
- Converge (a diferencia de la suma de inversos de todos los primos)

**Espiral de Ulam (1963)**
- Stanislaw Ulam dibujó números naturales en espiral
- Los primos forman patrones diagonales sorprendentes
- No se entiende completamente por qué

### Distribución

**Brecha entre primos**
- Entre 113 y 127 hay 13 números compuestos
- La brecha promedio cerca de \( n \) es \( ≈ \\ln(n) \)
- ¡Pero pueden haber brechas arbitrariamente grandes!

**Probabilidad**
- La probabilidad de que un número cercano a \( n \) sea primo: \( ≈ 1/\\ln(n) \)
- Para \( n = 1,000,000 \): probabilidad \( ≈ 7.2\\% \)
- Para \( n = 1,000,000,000 \): probabilidad \( ≈ 4.8\\% \)

### En la Cultura

**Literatura**
- "La soledad de los números primos" (Paolo Giordano)
- "El curioso incidente del perro a medianoche" (Mark Haddon) - capítulos numerados con primos

**Cine**
- "Pi" (Darren Aronofsky, 1998)
- "Una mente brillante" (Ron Howard, 2001)

**Recompensas**
- $150,000 por encontrar un primo de >100 millones de dígitos
- $250,000 por >1,000 millones de dígitos
- (Electronic Frontier Foundation)
"""

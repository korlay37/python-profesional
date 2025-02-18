"""
Crearemos un script(programa) que analice descripciones de empleo para ver que piden
y optimizar nuestras aplicaciones
1 Crear un decorador que mida el tiempo de ejecucion de una funcion
e imprimirlo / meterlo en un log
2 Crear un generador: leer_lineas, recibe el texto y devuelve una linea del texto a la vez
3 Crear una funcion procesar_texto recibe el texto y:
    - Retorna una lista de palabras( usando comprension de listas)
    - Las palabras son de almenos 3 caracteres (re.findall())
    - La palabra no esta en la lista de IGNORE_WORDS
    - La palabra esta en la lista de KEYWORDS
    NOTA: CHECAR COINCIDENCIAS PARCIALES O EXACTAS CON KEYWORDS
4 Crear una funcion contar_palabras recibe la lista de palabras de procesar texto,
    - Utiliza de collections, Counter para contar frecuencia,
    - Devuelve un diccionario de las 10 mas comunes: counter.most_common(10)
    (esto dara como llave la palabra y valor las frecuencia)

5 Corre el codigo:

palabras_clave = procesar_texto(descripcion_empleo)
top_palabras = contar_palabras(palabras_clave)
print("\nPalabras clave más relevantes:")
for palabra, frecuencia in top_palabras.items():
    print(f"{palabra}: {frecuencia} veces")
"""

import time
import re
from collections import Counter
from typing import Callable, Generator, Any

IGNORE_WORDS = {
    "con", "en", "y", "de", "la", "el", "a", "que", "un", "una", "los", "las", "por", "para", "es",
    "son", "se", "o", "tipo", "experiencia", "conocimientos", "habilidades", "deseable", "dominio",
    "funciones", "desarrollo", "servicios"
}

KEYWORDS = {
    "python", "django", "flask", "rest", "sql", "mysql", "postgresql", "git", "docker",
    "kubernetes", "aws", "azure", "gcp", "rest", "graphql", "typescript", "javascript",
    "react", "vue", "angular", "html", "css", "sass", "ci/cd","front-end", "back-end"
}

# Decorador para medir tiempo de ejecucion
def medir_tiempo(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        inicio: float = time.time()
        resultado: Any = func(*args, **kwargs)
        fin: float = time.time()
        print(f"Tiempo de ejecucion de {func.__name__}: {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

# Generador para leer lineas sin cargar todo en memoria
def leer_lineas(texto: str) -> Generator:
    for linea in texto.split("\n"):
        yield linea

# Funcion para procesar y limpiar el texto
@medir_tiempo
def procesar_texto(texto: str) -> list[str]:
    palabras: list[str] = [
        palabra.lower()
        for linea in leer_lineas(texto)
        for palabra in re.findall(r"\b[a-zA-Z]{3,}\b", linea)
        if palabra.lower() not in IGNORE_WORDS and (
            any(keyword in palabra.lower() for keyword in KEYWORDS)
            or palabra.lower() in KEYWORDS
        )
    ]
    return palabras

#  Funcion para contar palabras clave y frecuencia
@medir_tiempo
def contar_palabras(palabras: list[str]) -> dict:
    frecuencia: Counter = Counter(palabras)
    return dict(frecuencia.most_common(10))

descripcion_empleo = """
Sobre el Puesto
Estamos en la búsqueda de un Full Stack Developer con experiencia en React y Python para unirse a nuestro equipo. 
Trabajarás en el desarrollo de aplicaciones escalables, asegurando el rendimiento óptimo tanto en el frontend como en el backend.

Responsabilidades
Diseñar y desarrollar interfaces interactivas utilizando React.
Construir y optimizar APIs con Python y Django o Flask.
Implementar bases de datos eficientes con PostgreSQL o MongoDB.
Integrar servicios en la nube como AWS o Azure para mejorar el rendimiento.
Colaborar con equipos de diseño y producto para ofrecer soluciones innovadoras.
Escribir código limpio y modular utilizando JavaScript/TypeScript en el frontend.
Implementar y mantener procesos de CI/CD para automatizar despliegues.
Optimizar el rendimiento de aplicaciones utilizando herramientas como Docker y Kubernetes.
Requisitos Técnicos
React con experiencia en hooks y estado global (Redux/Zustand).
Desarrollo backend con Python y frameworks como Django o Flask.
Experiencia en bases de datos SQL y NoSQL (PostgreSQL, MongoDB).
Conocimiento de arquitecturas basadas en APIs REST y GraphQL.
Manejo de sistemas de control de versiones como Git.
Experiencia con herramientas de contenedores (Docker, Kubernetes).
Conocimientos en metodologías ágiles (Scrum, Kanban).

Deseable
Experiencia con Next.js para SSR y optimización de aplicaciones en React.
Conocimientos en infraestructura en la nube (AWS Lambda, S3, EC2).
Familiaridad con herramientas de monitoreo y logging (Grafana, Prometheus).
"""

palabras_clave = procesar_texto(descripcion_empleo)
top_palabras = contar_palabras(palabras_clave)
print("\nPalabras clave más relevantes:")
for palabra, frecuencia in top_palabras.items():
    print(f"{palabra}: {frecuencia} veces")
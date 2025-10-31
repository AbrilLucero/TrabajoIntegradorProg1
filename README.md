readme
#UTN/Trabajo Práctico Integrador (TPI)/TUP

Acosta Critina / Lucero Abril

Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas Tecnologías utilizadas

Python 3.13.2 CSV (manejo de archivos) Funciones y estructuras de datos Git / GitHub (control de versiones y entrega)

#Objetivo del proyecto:

Desarrollar una aplicación en Python que permita gestionar información sobre países, aplicando:

Listas y diccionarios
Funciones y modularización
Estructuras condicionales y repetitivas
Técnicas de filtrado, ordenamiento y generación de estadísticas
El sistema lee los datos desde un archivo CSV y permite realizar consultas, obtener indicadores clave y mostrar resultados de forma clara y organizada.

#Estructura de datos del proyecto .API.py Conexión y carga de datos desde la API REST Countries .menú.py Interfaz principal del programa (menú interactivo) .paises.csv Archivo local con los datos de los países Modulo .Buscar_por_nombre.py (Búsquedas por nombre total o parcial) .estadisticas.py (Funciones de estadísticas y promedios) .funciones_filtrado.py (Funciones de filtros personalizados) .funciones_ordenamiento.py (Funciones de ordenamiento por distintos criterios) pycache/ Archivos compilados automáticamente

#Funcionalidades principales

Solicitud a la API: El programa realiza una petición con el módulo requests de Python.

Conversión a estructuras de Python: La respuesta en formato JSON se transforma en una lista de diccionarios, donde cada elemento representa un país con sus datos asociados.

Almacenamiento local: Los datos se exportan a un archivo CSV.

Filtros y búsquedas Permite buscar países por nombre (completo o parcial) y filtrar por continente.

Ordenamientos Ordena los países por nombre, población o superficie.

Estadísticas

Promedio de población por continente
Cantidad de países por continente
Densidad poblacional promedio
Validaciones y control de errores
Ingreso de datos controlado y manejo de errores básicos para garantizar estabilidad.

TUP1_INTEGRADOR

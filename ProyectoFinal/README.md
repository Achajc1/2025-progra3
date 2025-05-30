# Documentación del Proyecto Final

## Nombre del proyecto

**Sistema de Recomendación Turística con Visualización y Estructuras de Datos**

## Autor

Andrés Chaj

## Curso

Programación III - Universidad Mariano Gálvez

---

## Introducción

Este proyecto fue desarrollado como trabajo final del curso Programación III. Consiste en un sistema que permite al usuario:

* Cargar lugares turísticos y de hospedaje desde archivos CSV o manualmente.
* Calificar los lugares.
* Obtener recomendaciones de viaje basadas en presupuesto, tiempo y ubicación.
* Visualizar las rutas en un mapa.
* Exportar recomendaciones y estructuras a archivos CSV o imagen (Graphviz).

El sistema está desarrollado en Python y utiliza estructuras como Árbol B y grafos para organizar y procesar los datos.

---

## Requisitos

* Python 3.10 o superior
* Bibliotecas:

  * `graphviz`
  * `folium`
  * `csv`, `os`, `datetime`
  * (Opcional) Google Chrome para ver las visualizaciones

---

## Manual de Usuario

### 1. Iniciar el programa

Ejecutar el archivo `main.py`. Se mostrará un menú principal con las opciones disponibles.

### 2. Cargar datos desde CSV

Selecciona la opción 1. Esto carga los lugares desde un archivo ubicado en `data/lugares.csv`. Se deben incluir columnas como nombre, tipo, latitud, longitud, etc.

### 3. Agregar lugar manualmente

Selecciona la opción 2. Ingresar los datos que se piden en pantalla. El lugar se guardará en el Árbol B.

### 4. Obtener recomendaciones y ver mapa

Selecciona la opción 3. Ingresar la ubicación (latitud y longitud), presupuesto diario y cantidad de días. El sistema calculará las mejores opciones y las mostrará en un mapa.

### 5. Exportar recomendaciones a CSV

Selecciona la opción 4. Si ya se han generado recomendaciones, estas se exportarán a un archivo con fecha y hora en la carpeta `data/recomendaciones`.

### 6. Exportar Árbol B a imagen

Selecciona la opción 5. Se exportará el árbol en formato PNG usando Graphviz, mostrando la estructura de los lugares insertados.

### 7. Exportar grafo de rutas

Selecciona la opción 6. El grafo con los caminos entre los lugares recomendados se guarda como imagen PNG.

---

## Estructura del Proyecto

```
ProyectoFinal/
├── data/
│   ├── lugares.csv
│   ├── recomendaciones/
│   └── lugares_exportados/
├── estructuras/
│   ├── arbol_b.py
│   └── grafo.py
├── interfaz/
├── logica/
│   ├── exportador.py
│   ├── grafo_util.py
│   ├── interacciones_usuario.py
│   ├── lugar.py
│   ├── visualizador_arbol_b.py
│   ├── visualizador_grafo.py
│   └── visualizador_mapa.py
├── mapas/
├── Pruebas/
└── main.py
```

---

## Implementación

### Arbol B

Se utilizó un Árbol B para almacenar los lugares de forma ordenada por ID. Se pueden insertar y recuperar lugares de forma eficiente.

### Grafo

Los lugares se conectan con un grafo ponderado. Cada nodo representa un lugar y las aristas la distancia entre ellos. Se usa Dijkstra para encontrar rutas recomendadas.

### Recomendaciones

Se calculan a partir de:

* Distancia desde el origen
* Presupuesto total
* Tiempo disponible

### Visualización

* Se usan mapas con `folium` para mostrar los lugares recomendados.
* Se generan archivos PNG con `graphviz` para ver el Árbol B y el grafo.

---

## Diagrama UML (simplificado)

```
+-------------------+
| Lugar             |
+-------------------+
| id, nombre, tipo  |
| latitud, longitud|
| precio, calificacion|
| tiempo_estadia    |
+-------------------+

+-------------------+
| ArbolB            |
+-------------------+
| insertar()        |
| obtener_todos()   |
+-------------------+

+-------------------+
| Grafo             |
+-------------------+
| agregar_nodo()    |
| agregar_arista()  |
| vecinos()         |
+-------------------+

+---------------------------+
| Recomendador             |
+---------------------------+
| recomendar_ruta()        |
+---------------------------+
```

---

## Conclusión

Este proyecto integró varios conocimientos vistos en el curso, como estructuras de datos, algoritmos de búsqueda, manejo de archivos, visualización de datos y más.

Gracias por revisar este trabajo :D

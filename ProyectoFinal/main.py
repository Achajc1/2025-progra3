from estructuras.arbol_b import ArbolB
from logica.manejador_datos import cargar_lugares_desde_csv
from logica.visualizador_mapa import mostrar_recomendaciones_en_mapa
from logica.grafo_util import construir_grafo_desde_arbol, recomendar_ruta
from logica.exportador import exportar_recomendaciones_csv
from logica.visualizador_arbol_b import exportar_arbol_b
from logica.visualizador_grafo import exportar_grafo
from logica.interacciones_usuario import agregar_lugar_manual

def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Cargar datos desde CSV")
    print("2. Agregar lugar manualmente")
    print("3. Obtener recomendaciones y ver mapa")
    print("4. Exportar recomendaciones a CSV")
    print("5. Exportar estructura del Árbol B (Graphviz)")
    print("6. Exportar grafo de rutas (Graphviz)")
    print("0. Salir")

if __name__ == "__main__":
    arbol = ArbolB(grado=2)
    grafo = None
    recomendaciones = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            cargar_lugares_desde_csv("data/lugares.csv", arbol, "Turístico")
            cargar_lugares_desde_csv("data/lugares.csv", arbol, "Hospedaje")
            grafo = construir_grafo_desde_arbol(arbol)
            print("✔ Datos cargados y grafo construido.")
        
        elif opcion == "2":
            agregar_lugar_manual(arbol)
            grafo = construir_grafo_desde_arbol(arbol)

        elif opcion == "3":
            if grafo is None:
                print("❌ Primero debes cargar los datos (opción 1) o agregar al menos un lugar (opción 2).")
                continue

            try:
                lat = float(input("Tu latitud: "))
                lon = float(input("Tu longitud: "))
                dias = int(input("Días disponibles: "))
                presupuesto = float(input("Presupuesto diario (Q): "))
                total = presupuesto * dias
                origen = (lat, lon)

                recomendaciones = recomendar_ruta(grafo, origen, total, dias)
                if recomendaciones:
                    mostrar_recomendaciones_en_mapa(recomendaciones, origen)
                else:
                    print("❌ No se encontraron lugares que coincidan con tus criterios.")
            except ValueError:
                print("❌ Entrada inválida.")

        elif opcion == "4":
            if recomendaciones:
                exportar_recomendaciones_csv(recomendaciones)
            else:
                print("❌ No hay recomendaciones para exportar.")

        elif opcion == "5":
            exportar_arbol_b(arbol)

        elif opcion == "6":
            if grafo:
                exportar_grafo(grafo)
            else:
                print("❌ Primero debes cargar datos y construir el grafo.")

        elif opcion == "0":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

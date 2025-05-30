import folium
import webbrowser
import os

def mostrar_recomendaciones_en_mapa(lugares, origen):
    if not lugares:
        print("No hay lugares recomendados para mostrar.")
        return

    mapa = folium.Map(location=origen, zoom_start=12)

    # Marcador de origen
    folium.Marker(
        location=origen,
        popup="Tu ubicación",
        icon=folium.Icon(color="green", icon="home")
    ).add_to(mapa)

    # Marcadores de lugares recomendados
    for lugar in lugares:
        folium.Marker(
            location=(lugar.latitud, lugar.longitud),
            popup=f"{lugar.nombre}\nQ{lugar.precio} | {lugar.tiempo_estadia} días",
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(mapa)

    # Guardar y abrir mapa
    mapa.save("mapa_recomendaciones.html")
    webbrowser.open('file://' + os.path.realpath("mapa_recomendaciones.html"))


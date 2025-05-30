class Lugar:
    def __init__(self, id, nombre, tipo, latitud, longitud, precio, calificacion, tiempo_estadia=None):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo  # "Hospedaje" o "Turístico"
        self.latitud = float(latitud)
        self.longitud = float(longitud)
        self.precio = float(precio) if precio not in (None, '', '-') else None  # <- Se asegura que precio esté definido
        self.calificacion = float(calificacion) if calificacion not in (None, '', '-') else None
        self.tiempo_estadia = float(tiempo_estadia) if tiempo_estadia not in (None, '', '-') else None

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


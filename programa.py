# programa.py
# Genera un archivo KML con parámetros personalizados

def generar_kml(nombre_archivo, nombre_punto, descripcion, lon, lat):
    contenido = f"""<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2">
      <Placemark>
        <name>{nombre_punto}</name>
        <description>{descripcion}</description>
        <Point>
          <coordinates>{lon},{lat},0</coordinates>
        </Point>
      </Placemark>
    </kml>"""

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(contenido)

if __name__ == "__main__":
    # Ejemplo por defecto (para probar fuera del navegador)
    generar_kml("resultado.kml", "Punto de ejemplo", "Generado desde Python", -70.65, -33.44)
    print("Archivo KML generado correctamente.")



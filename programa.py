# programa.py
# Script de ejemplo compatible con Pyodide
# Genera un archivo KML sencillo

def generar_kml(nombre_archivo="resultado.kml"):
    contenido = """<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2">
      <Placemark>
        <name>Punto de ejemplo</name>
        <description>Generado con Pyodide en el navegador</description>
        <Point>
          <coordinates>-70.6503,-33.4372,0</coordinates>
        </Point>
      </Placemark>
    </kml>"""

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(contenido)

# Ejecutar directamente si se llama el script
if __name__ == "__main__":
    generar_kml()
    print("Archivo KML generado correctamente.")



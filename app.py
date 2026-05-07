from flask import Flask, render_template, request
from Carretera_USC import buscar_solucion_UCS
from arbol import Nodo

app = Flask(__name__)

# Tus conexiones
conexiones = {
    'JILOYORK': {'CDMX': 125, 'QRO': 513},
    'MORELOS': {'QRO': 524},
    'CDMX': {'JILOYORK': 125, 'QRO': 433, 'HIDALGO': 491},
    'HIDALGO': {'CDMX': 491, 'QRO': 356, 'MEXICALI': 309, 'MONTERREY': 346},
    'QRO': {
        'SLP': 203,
        'MORELOS': 514,
        'JILOYORK': 513,
        'CDMX': 433,
        'MONTERREY': 603,
        'SONORA': 437,
        'HIDALGO': 356,
        'MEXICALI': 313,
        'AGUASCALIENTES': 599
    },
    'SLP': {'AGUASCALIENTES': 390, 'QRO': 203},
    'AGUASCALIENTES': {'SLP': 390, 'QRO': 599},
    'SONORA': {'SLP': 437, 'QRO': 437, 'MEXICALI': 394},
    'MEXICALI': {'MONTERREY': 296, 'HIDALGO': 309, 'QRO': 313},
    'MONTERREY': {'MEXICALI': 296, 'QRO': 603, 'HIDALGO': 346}
}

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        inicio = request.form["inicio"].upper()
        destino = request.form["destino"].upper()

        nodo_solucion = buscar_solucion_UCS(conexiones, inicio, destino)

        if nodo_solucion:
            ruta = []
            nodo = nodo_solucion

            while nodo is not None:
                ruta.append(nodo.get_datos())
                nodo = nodo.get_padre()

            ruta.reverse()

            resultado = f"Ruta: {' → '.join(ruta)} | Costo: {nodo_solucion.get_costo()}"
        else:
            resultado = "No se encontró ruta"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
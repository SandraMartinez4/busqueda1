from arbol import Nodo

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_costo(0)

    nodos_frontera = [nodo_inicial]
    nodos_visitados = []

    while len(nodos_frontera) != 0:
        nodos_frontera = sorted(nodos_frontera, key=lambda x: x.get_costo())
        nodo_actual = nodos_frontera.pop(0)

        nodos_visitados.append(nodo_actual)

        if nodo_actual.get_datos() == solucion:
            return nodo_actual

        for destino in conexiones[nodo_actual.get_datos()]:
            hijo = Nodo(destino)
            costo = conexiones[nodo_actual.get_datos()][destino]

            hijo.set_costo(nodo_actual.get_costo() + costo)
            hijo.set_padre(nodo_actual)

            if not hijo.en_lista(nodos_visitados):
                if not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)
                else:
                    for n in nodos_frontera:
                        if n.igual(hijo) and n.get_costo() > hijo.get_costo():
                            nodos_frontera.remove(n)
                            nodos_frontera.append(hijo)

    return None

if __name__ == "__main__":
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

    estado_inicial = 'JILOYORK'
    solucion = 'AGUASCALIENTES'

    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)

    resultado = []
    nodo = nodo_solucion

    while nodo is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.reverse()

    print("Ruta:", resultado)
    print("Costo:", nodo_solucion.get_costo())
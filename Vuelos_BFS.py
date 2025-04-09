# Vuelos con busqueda en amplitud 
from Arbol import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while(not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera[0]
        #Extraer nodo y añadorlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            #Solucion encontrada
            solucion = True
            return nodo  
        else:
            # Expandir los nodos hijos
            dato_nodo = nodo.get_datos()
            
            for un_hijo in conexiones.get(dato_nodo):  
                hijo = Nodo(un_hijo, nodo)  
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)


if __name__ == "__main__":
    conexiones = {
        'CDMX': {'SLP', 'MEXICALI', 'CHIHUAHUA'},
        'SAPOPAN': {'ZACATECAS', 'MEXICALI'},
        'GUADALAJARA': {'CHIAPAS'},
        'CHIAPAS': {'CHIHUAHUA'},
        'MEXICALI': {'SLP', 'SAPOPAN', 'CDMX', 'CHIHUAHUA', 'SONORA'},
        'SLP': {'CDMX', 'MEXICALI'},
        'ZACATECAS': {'SAPOPAN', 'SONORA', 'CHIHUAHUA'},
        'SONORA': {'ZACATECAS', 'MEXICALI'},
        'MICHOACAN': {'CHIHUAHUA'},
        'CHIHUAHUA': {'MEXICALI', 'ZACATECAS', 'CDMX', 'CHIAPAS'}
    }

    estado_inicial = 'CDMX'
    solucion = 'ZACATECAS'
    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)

    # Mostrar resultados
    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion  # Se usa nodo_solucion en lugar de nodo no definido
        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.reverse()
        print(resultado)
    else:
        print("No se encontró una solución.")

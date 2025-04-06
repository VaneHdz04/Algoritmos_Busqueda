from Arbol import Nodo

def buscar_solucion_BFS_rec(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())

    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial  
    else:
        # Expandir los nodos sucesores (hijos)
        dato_nodo = nodo_inicial.get_datos()
        hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]], nodo_inicial)
        hijo_central = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]], nodo_inicial)
        hijo_derecho = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]], nodo_inicial)

        #Agregamos los hijos a la lista en lugar de usar set_hijos(), no existe set_hijos en Arbol 
        nodo_inicial.hijos.extend([hijo_izquierdo, hijo_central, hijo_derecho])

        for nodo_hijo in nodo_inicial.hijos:  #Usamos nodo_inicial.hijos
            if not nodo_hijo.get_datos() in visitados:
                # Llamada Recursiva
                sol = buscar_solucion_BFS_rec(nodo_hijo, solucion, visitados)
                if sol != None:
                    return sol

        return None  

if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]  
    solucion = [1, 2, 3, 4]
    nodo_solucion = []
    visitados = []
    nodo_inicial = Nodo(estado_inicial)
    nodo = buscar_solucion_BFS_rec(nodo_inicial, solucion, visitados)

    # Mostrar resultados tenia eror en las identaciones 
    if nodo: # Agregue un if
        resultado = []
        while nodo.get_padre() != None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)  
        resultado.reverse()
        print(resultado)  

import random

class Grafo:
    def __init__(self):
        self.grafo_dict = {} # Diccionario para almacenar el grafo

    def agregar_vertice(self, vertice): # Método para agregar vértices
        if vertice not in self.grafo_dict:
            self.grafo_dict[vertice] = []

    def agregar_arista(self, v1, v2): # Método para agregar aristas
        if v1 not in self.grafo_dict or v2 not in self.grafo_dict:
            raise ValueError("Uno o ambos vértices no existen en el grafo.")
        self.grafo_dict[v1].append(v2)
        self.grafo_dict[v2].append(v1)

    def encontrar_ruta_euleriana(self): # Método para encontrar la ruta euleriana
        vertices_grado_impar = [vertice for vertice in self.grafo_dict if len(self.grafo_dict[vertice]) % 2 != 0]
        if len(vertices_grado_impar) > 2:
            return None  # No hay ruta euleriana

        # Seleccionar un vértice inicial aleatorio
        vertice_inicial = random.choice(list(self.grafo_dict.keys()))

        ruta = [] # Lista para almacenar la ruta euleriana
        pila = [vertice_inicial] # Pila para almacenar los vértices visitados
        while pila:
            vertice = pila[-1]
            # Si hay vértices adyacentes sin visitar
            if self.grafo_dict[vertice]:  
                siguiente_vertice = self.grafo_dict[vertice][0] # Seleccionar un vértice adyacente
                pila.append(siguiente_vertice) # Agregar a la pila
                self.grafo_dict[vertice].remove(siguiente_vertice) # Eliminar el arista
                self.grafo_dict[siguiente_vertice].remove(vertice) # Eliminar el arista
            else:
                ruta.append(pila.pop())
        return vertice_inicial, ruta[::-1]  # Invertir la ruta para obtener el orden correcto

g = Grafo() # Crear un objeto de la clase Grafo
vertices = ['A', 'B', 'C', 'D', 'E', 'F'] # Lista de vértices
for vertice in vertices:
    g.agregar_vertice(vertice)

g.agregar_arista('A', 'B')
g.agregar_arista('A', 'C')
g.agregar_arista('A', 'D')
g.agregar_arista('A', 'E')
g.agregar_arista('B', 'D')
g.agregar_arista('C', 'D')
g.agregar_arista('C', 'E')
g.agregar_arista('C', 'F')
g.agregar_arista('D', 'F')

vertice_inicial, ruta_euleriana = g.encontrar_ruta_euleriana() # Llamamos al método encontrar_ruta_euleriana

if ruta_euleriana:
    print(f"Ruta Euleriana: {' -> '.join(ruta_euleriana)}") # Imprimimos la ruta euleriana
else:
    print("No hay ruta Euleriana.") # Imprimimos que no hay ruta euleriana
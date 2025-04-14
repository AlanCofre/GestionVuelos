class Nodo:
    def __init__(self,vuelo):
        self.vuelo = vuelo     # Objeto vuelo
        self.anterior = None   # Nodo anterior
        self.siguiente = None  # Nodo siguiente

# guarda una instancia del modelo vuelo, no solo datos datos
# permite conexion doble hacia adelante y atras
# se usará internamente en la clase ListaVuelos 
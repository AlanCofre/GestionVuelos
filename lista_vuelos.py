from nodo import Nodo
from models import Vuelo
from sqlalchemy.orm import Session

class ListaVuelos:
    def __init__(self, session: Session):
        self.cabeza = None       #primer nodo
        self.cola  = None        #ulitmo nodo
        self.size = 0            # Tamaño actual
        self.session = session   # Sesion SQlalchemy 
    
    def longitud(self):
        return self.size
    
    def insertar_al_frente(self, vuelo: Vuelo):
        nuevo = Nodo(vuelo)
        nuevo.siguiente = self.cabeza
        if self.cabeza is not None:
            self.cabeza.anterior = nuevo
        else:
            self.cola = nuevo #primer nodo si la lista esta vacia    
        self.cabeza = nuevo
        self.size += 1
        self.session.add(vuelo)
        self.session.commit()
    
    def insertar_al_final(self, vuelo: Vuelo):
        nuevo = Nodo(vuelo)
        nuevo.anterior = self.cola
        if self.cola is not None:
            self.cola.siguiente = nuevo
        else:
            self.cabeza = nuevo
        self.cola = nuevo
        self.size += 1
        self.session.add(vuelo)
        self.session.commit()
    
    def obtener_primero(self):
        return self.cabeza.vuelo if self.cabeza else None

    def obtener_ultimo(self):
        return self.cola.vuelo if self.cola else None
    
    def insertar_en_posicion(self, vuelo: Vuelo, posicion: int):
        if posicion <= 0:
            return self.insertar_al_frente(vuelo)
        if posicion >= self.size:
            return self.insertar_al_final(vuelo)
        
        actual = self.cabeza
        for _ in range(posicion):
            actual.siguiente
        
        nuevo = Nodo(vuelo)
        anterior = actual.anterior

        nuevo.anterior = anterior
        nuevo.siguiente = actual
        anterior.siguiente = nuevo
        actual.anterior = nuevo

        self.size += 1
        self.session.add(vuelo)
        self.session.commit()

    def extraer_de_posicion(self, posicion: int):
        if posicion < 0 or posicion >= self.size:
            return None

        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente

        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        else:
            self.cabeza = actual.siguiente
        
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        else:
            self.cola = actual.anterior

        self.size -= 1  
        vuelo = actual.vuelo
        self.session.delete(vuelo)
        self.session.commit()
        return vuelo

    def listar_vuelos(self):
        vuelos = []
        actual = self.cabeza
        while actual:
            vuelos.append(actual.vuelo)
            actual = actual.siguiente
        return vuelos

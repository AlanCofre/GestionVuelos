from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import init_db, SessionLocal
from models import Vuelo, EstadoVuelo 
from lista_vuelos import ListaVuelos
from datetime import datetime

# Iniciar base de datos y app
init_db()
app = FastAPI()
lista = None # Se creará al iniciar la app con la sesion

# Obtener sesion 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Inicializar ListaVuelos al iniciar
@app.on_event("startup")
def startup():
    global lista
    db = SessionLocal()
    lista = ListaVuelos(db)

# ENDPOINTS

@app.post("/vuelos")
def agregar_vuelo(vuelo: dict):
    nuevo = Vuelo(
        codigo=vuelo["codigo"],
        estado=EstadoVuelo(vuelo["estado"]),
        hora=datetime.fromisoformat(vuelo["hora"]),
        origen=vuelo["origen"],
        destino=vuelo["destino"]
    )

    if nuevo.estado == EstadoVuelo.emergencia:
        lista.insertar_al_frente(nuevo)
    else:
        lista.insertar_al_final(nuevo)
    return {"mensaje": "Vuelo agregado"}

@app.get("/vuelos/total")
def cantidad_vuelos():
    return {"total": lista.longitud()}

@app.get("/vuelos/proximo")
def vuelo_primero():
    vuelo = lista.obtener_primero()
    if vuelo is None:
        raise HTTPException(status_code=404, detail="Sin vuelos") 
    return vuelo

@app.get("/vuelos/ultimo")
def vuelo_ultimo():
    vuelo = lista.obtener_ultimo()
    if vuelo is None:
        raise HTTPException(status_code=404, detail="Sin vuelos") 
    return vuelo

@app.post("/vuelos/inserta")
def insertar_en_posicion(vuelo: dict, posicion: int):
    nuevo = Vuelo(
        codigo=vuelo["codigo"],
        estado=EstadoVuelo(vuelo["estado"]),
        hora=datetime.fromisoformat(vuelo["hora"]),
        origen=vuelo["origen"],
        destino=vuelo["destino"]
    )
    lista.insertar_en_posicion(nuevo, posicion)
    return {"mensaje": f"Vuelo insertado en posicion {posicion}"}

@app.delete("/vuelo/extraer")
def eliminar_vuelo(posicion: int):
    vuelo = lista.extraer_de_posicion(posicion)
    if vuelo is None:
        raise HTTPException(status_code=404, detail="Posicion invalida")
    return {"mensaje": f"Vuelo {vuelo.codigo} eliminado"}

@app.get("/vuelos/lista")
def listar():
    return lista.listar_vuelos()
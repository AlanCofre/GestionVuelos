from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class EstadoVueloEnum(str, Enum):
    progamado = "programado"
    emergencia = "emergencia"
    retrasado = "retrasado"

class VueloSchema(BaseModel):
    codigo: str
    estado: EstadoVueloEnum
    hora: datetime
    origen: str
    destino: str

class VueloOut(VueloSchema):
    class Config:
        orm_mode = True






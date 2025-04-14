from sqlalchemy import Column, String, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class EstadoVuelo(enum.Enum):
    programado = "programado"
    emergencia = "emergencia"
    retrasado = "retrasado"

class Vuelo(Base):
    __tablename__ = "vuelos"

    codigo = Column(String, primary_key= True, unique= True)
    estado = Column(Enum,(EstadoVuelo), nullable= False)
    hora = Column(DateTime, nullable= False)
    origen = Column(String, nullable= False)
    destino = Column(String, nullable= False) 

    def __repr__(self):
        return f"<Vuelo(codigo={self.codigo}, estado={self.estado}, origen={self.origen}, destino={self.destino})>"
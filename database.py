from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

#Motor SQLite en local
DATABASE_URL = "sqlite:///.vuelos.db"

engine = create_engine(DATABASE_URL, conect_args={"chek_same_thread": False})

#Cerrar sesión
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

#Crear las tablas
def init_db():
    Base.metadata.create_all(bind=engine)
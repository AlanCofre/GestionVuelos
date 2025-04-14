from database import init_db, SessionLocal

# Inicializamos la base de datos y crea las tabla si no existen
init_db()

# Confirmamos si funciona
db = SessionLocal()
print("Conexion exitosa a la base de datos")
db.close
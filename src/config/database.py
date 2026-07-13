import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

# Especifica la ruta local apuntando a la instancia Express
DB_SERVER = "localhost\\SQLEXPRESS"  
DB_DATABASE = "gestor_tareas"  # Reemplaza con el nombre real de tu BD

# La URL limpia sin el puerto 1433
DATABASE_URL = (
    f"mssql+pyodbc://@{DB_SERVER}/{DB_DATABASE}"
    f"?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

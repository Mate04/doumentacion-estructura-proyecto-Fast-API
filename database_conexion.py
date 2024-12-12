from sqlmodel import create_engine,SQLModel

engine = create_engine("sqlite:///databasenueva.db")
# Aca se pone la siguiente linea unicamente para crear el esquema
SQLModel.metadata.create_all(engine)
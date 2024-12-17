
from fastapi import FastAPI

app = FastAPI()

#hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")

@app.get("/")
def get_hero_name_secret():
    return {"Hello":"World"}
from model.team import Team
from model.hero import Hero 
from repository.repository_team import TeamRepository
from repository.repository_hero import HeroRepository
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
app = FastAPI()

hero_repo = HeroRepository()


@app.get("/")
def hola_mundo():
    return {"hello":"world"}

@app.post("/")
def create_heroe():
    return {"hello":"world"}


#hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
#hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

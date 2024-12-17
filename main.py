from fastapi import FastAPI
from schemas.hero_schema import HeroCreateDTO, HeroResponse
from service.service_hero import HeroService
app = FastAPI()
service_hero = HeroService()


@app.post("/hero", response_model=HeroResponse, response_model_exclude_unset=True)
def create_heroe(hero:HeroCreateDTO):
    new_hero = service_hero.add_heroe(hero)
    return new_hero



@app.get("/hero")
def get_hero_name_secret(name:int):
    return {
        "name":name
        }
@app.get("/hero/{id}")
def get_hero_name(id:int):
    return {
        "name":id
        }
#hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
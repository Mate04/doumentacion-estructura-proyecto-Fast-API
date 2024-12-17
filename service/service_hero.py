from model.hero import Hero
from repository.repository_hero import HeroRepository
from schemas.hero_schema import HeroCreateDTO
from fastapi import HTTPException, status

repository_hero = HeroRepository()

class HeroService:
    def __init__(self):
        self.repository = repository_hero
    def findByNameSecrect(self,name_secret:str) -> Hero:
        hero = self.repository.findByNameSecret(name=name_secret)
        if (hero ==None):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se entro heroe con nombre {name_secret}")
        return hero
    
    def add_heroe(self, hero:HeroCreateDTO) -> Hero:

        resultado = self.repository.findByName(hero.name)
        if (resultado != None):
            return "Ya existe este nombre"
        hero_new = Hero(name=hero.name,secret_name=hero.secret_name, age=hero.age )
        hero_new = self.repository.add(hero_new)

        return hero_new
    def find_by_id(self, id:int) -> Hero:
        resultado = self.repository.get(id)
        if (resultado ==None):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se entro heroe con id {id}")
        return resultado

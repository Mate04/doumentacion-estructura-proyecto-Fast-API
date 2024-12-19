from fastapi import APIRouter
from schemas.hero_schema import HeroCreateDTO, HeroResponse
from service.service_hero import HeroService

router = APIRouter( prefix="/hero",tags=["hero"])
service_hero = HeroService()

# Definir rutas para el router
@router.get("/{id}",response_model=HeroResponse, response_model_exclude_unset=True)
def get_hero_name(id:int):
    """
    ### Trae un heroe atravez de ID
    * id numerico
    """
    hero_found = service_hero.find_by_id(id)
    return hero_found

@router.post("/", response_model=HeroResponse, response_model_exclude_unset=True)
def create_heroe(hero:HeroCreateDTO):
    new_hero = service_hero.add_heroe(hero)
    return new_hero



@router.get("/",response_model=HeroResponse, response_model_exclude_unset=True)
def get_hero_name_secret(name_secret:str):
    hero_found = service_hero.findByNameSecrect(name_secret)
    return hero_found
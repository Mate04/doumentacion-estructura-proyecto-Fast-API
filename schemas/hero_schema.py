from pydantic import BaseModel, Field

# Aca es la entrada de la funcion
class HeroCreateDTO(BaseModel):
    name: str = Field(min_length=3,max_length=20)
    secret_name: str 
    age: int | None = Field(default=None, gt=5, lt=99)


class HeroResponse(BaseModel):
    id_hero: int
    name: str 
    secret_name: str 
    age: int | None 
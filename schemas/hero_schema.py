from pydantic import BaseModel, Field

# Aca es la entrada de la funcion
class HeroCreateDTO(BaseModel):
    name: str = Field(min_length=3,max_length=20)
    name_secret: str 
    age: int | None = Field(default=None, gt=5, lt=99)
from sqlmodel import SQLModel,Field ,Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from model.hero import Hero
class Team(SQLModel, table=True):
    id_team: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
    #Relaciones
    heroes: list["Hero"] = Relationship(back_populates="team")
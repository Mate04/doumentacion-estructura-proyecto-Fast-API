from sqlmodel import SQLModel,Field, Relationship
from typing import Optional


from model.team import Team

class Hero(SQLModel, table=True):
    id_hero: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

    #Relaciones
    team_id: int | None = Field(default=None, foreign_key="team.id_team")
    team: Team | None = Relationship(back_populates="heroes")
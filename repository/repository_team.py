from repository.repository_base import BaseRepository
from model.team import Team
from sqlmodel import select

class TeamRepository(BaseRepository[Team]):
    def __init__(self):
        super().__init__(Team)
    def findByName(self, name:str):
        with self.get_session() as session:
            query = select(Team).where(Team.name==name) 
            result =  session.exec(query).first()
            return result
    
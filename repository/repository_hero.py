from sqlmodel import select
from repository.repository_base import BaseRepository
from model.hero import Hero 

class HeroRepository(BaseRepository[Hero]):
    def __init__(self):
        super().__init__(Hero)


    def findByNameSecret(self, name:str):
        with self.get_session() as session:
            query = select(Hero).where(Hero.secret_name==name)
            result =  session.exec(query).first()
            return result
from typing import TypeVar, Generic, Type, List
from sqlmodel import Session, SQLModel
from database_conexion import engine


T = TypeVar("T", bound=SQLModel)



class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.engine  = engine
        self.model = model

    def get_session(self) -> Session:
        return Session(self.engine)  # Crea una nueva sesión


    def add(self, entity: T) -> T:
        with self.get_session() as session:
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity


    def get(self, entity_id: int) -> T:
        with self.get_session() as session:
            return session.get(self.model, entity_id)

    def get_all(self) -> List[T]:
        with self.get_session() as session:
            return session.query(self.model).all()


    def delete(self, entity_id: int) -> None:
        with self.get_session() as session:
            entity = session.get(self.model, entity_id)
            if entity:
                session.delete(entity)
                session.commit()

from sqlalchemy import Column, Integer, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base, declared_attr

Base = declarative_base()

class BaseModel(Base):
    """База для всех моделей."""


    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    __table_args__ = (PrimaryKeyConstraint('id'))
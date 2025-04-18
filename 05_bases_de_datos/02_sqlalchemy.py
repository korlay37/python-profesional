from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
from typing import Optional

# Crear base declarativa
Base = declarative_base()

# Crear motor
# "dialect+driver://username:password@host:port/database"
engine = create_engine("sqlite:///usuarios_orm.db", echo=True)
# engine = create_engine("sqlite:///:memory:")

class User(Base):
    __tablename__ = "users"

    id: Column[int] = Column(Integer, primary_key=True, autoincrement=True)
    name: Column[str] = Column(String, nullable=False)
    age: Column[int] = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, age={self.age})"
    
# Crear base de datos
Base.metadata.create_all(engine)

# Insertar y consultar
with Session(engine) as session:
    user1: User = User(name="Carlos", age=28)
    user2: User = User(name="Elena", age=34)

    session.add_all([user1, user2])
    session.commit()

    usuarios: list[User] = session.query(User).all()
    for usuario in usuarios:
        print(usuario)
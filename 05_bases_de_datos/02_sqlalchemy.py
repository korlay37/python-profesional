from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session, Mapped, mapped_column
from typing import Optional

# Crear base declarativa
Base = declarative_base()

# Crear motor
# "dialect+driver://username:password@host:port/database"
engine = create_engine("sqlite:///usuarios_orm.db")
# engine = create_engine("sqlite:///:memory:")

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, age={self.age})"
    
# Crear base de datos
Base.metadata.create_all(engine)

# Create
def agregar_usuario(nombre: str, edad: int) -> None:
    with Session(engine) as session:
        user: User = User(name=nombre, age=edad)
        session.add(user)
        session.commit()
        print(f"Usuario creadO: {user}")

# Read
def mostrar_usuarios() -> None:
    with Session(engine) as session:
        users: list[User] = session.query(User).all()
        for user in users:
            print(user)

def buscar_por_nombre(nombre: str) ->  Optional[User]:
    with Session(engine) as session:
        user: Optional[User] = session.query(User).filter(User.name == nombre).first()
        return user

# Update
def actualizar_edad(nombre: str, nueva_edad: int) -> None:
    with Session(engine) as session:
        user: Optional[User] = session.query(User).filter(User.name == nombre).first()
        if user:
            user.age = nueva_edad
            session.commit()
            print(f"Edad actualizada {user}")
        else:
            print("No se encontro usuario")

# Delete
def eliminar_usuario(nombre: str) -> None:
    with Session(engine) as session:
        user: User = session.query(User).filter(User.name == nombre).first()
        if user:
            session.delete(user)
            session.commit()
            print(f"Usuario borrado: {user}")
        else:
            print("Usuario no encontrado")

agregar_usuario("Paco", 20)
agregar_usuario("Josefina", 40)

mostrar_usuarios()

actualizar_edad("Josefina", 26)
user = buscar_por_nombre("Paco")
print(f"Encontre usuario: {user}")

eliminar_usuario("Paco")
mostrar_usuarios()


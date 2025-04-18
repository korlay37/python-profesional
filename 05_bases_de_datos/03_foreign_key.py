from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Session, Mapped, mapped_column, relationship
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
    posts = relationship("Post", back_populates="author")

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, age={self.age})"
    
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")

    def __repr__(self) -> str:
        return f"Post(id={self.id}, title={self.title})"

# Crear base de datos
Base.metadata.create_all(engine)

# Insertar datos
def crear_usuario_con_post(nombre: str, edad: int, titulo: str, contenido: str)-> None:
    try:
        with Session(engine) as session:
            user: User = User(name=nombre, age=edad)
            post: Post = Post(title=titulo, content=contenido, author=user)
            session.add_all([user, post])
            session.commit()
            print("Usuario y post creados")
    except Exception as e:
        print(f"Error al crear usuario o post: {e}")

def mostrar_posts_usuario(nombre: str) -> None:
    try:
        with Session(engine) as session:
            user: Optional[User] = session.query(User).filter_by(name=nombre).first()
            if user:
                print(f"Posts de {user.name}:")
                for post in user.posts:
                    print(f"  - {post.title}")
            else:
                print("Usuario no encontrado")
    except Exception as e:
        print(f"Error al consultar usuario por nombre: {e}")

def mostrar_posts_usuario_id(user_id: int) -> None:
    try:
        with Session(engine) as session:
            user: Optional[User] = session.get(User, user_id)
            if user:
                print(f"Posts de {user.name}:")
                for post in user.posts:
                    print(f"  - {post.title}")
            else:
                print("Usuario no encontrado")
    except Exception as e:
        print(f"Error al consultar usuario por nombre: {e}")

crear_usuario_con_post("Eduardo", 33, "Mi primer post", "Contenido del post aqui")
mostrar_posts_usuario("Eduardo")
print("===========================")
mostrar_posts_usuario_id(1)
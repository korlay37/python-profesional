from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, Session, Mapped, mapped_column, relationship
from typing import Optional


Base = declarative_base()
engine = create_engine("sqlite:///usuarios_orm.db")

association_table = Table(
    "user_course",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    courses = relationship("Course", secondary=association_table, back_populates="users")

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name})"

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    users = relationship("User", secondary=association_table, back_populates="courses")

    def __repr__(self) -> str:
        return f"Course(id={self.id}, title={self.title})"

# Crear base de datos
Base.metadata.create_all(engine)

def agregar_usuario(nombre: str) -> None:
    with Session(engine) as session:
        user: User = User(name=nombre)
        session.add(user)
        session.commit()
        print(f"Usuario creadO: {user}")

def inscribir_usuario_en_cursos(nombre: str, cursos: list[str]) -> None:
    with Session(engine) as session:
        user = session.query(User).filter_by(name=nombre).first()
        if not user:
            print("Usuario no encontrdo")
            return
        
        for titulo in cursos:
            course = session.query(Course).filter_by(title=titulo).first()
            if not course:
                course = Course(title=titulo)
                session.add(course)
            if course not in user.courses:
                user.courses.append(course)
        
        session.commit()
        print(f"Usuario {user.name} agregado a: {[c.title for c in user.courses]}")

def mostrar_cursos_de_usuario(nombre: str) -> None:
    with Session(engine) as session:
        user = session.query(User).filter_by(name=nombre).first()
        if user:
            print(f"Cursos de {user.name}:")
            for course in user.courses:
                print(f" - {course.title}")
        else:
            print("Usuario no encontrado")

def mostrar_usuarios_de_curso(titulo: str) -> None:
    with Session(engine) as session:
        course = session.query(Course).filter_by(title=titulo).first()
        if course:
            print(f"Users de {course.title}:")
            for user in course.users:
                print(f" - {user.name}")
        else:
            print("Curso no encontrado")

agregar_usuario("Eduardo")
agregar_usuario("Jose")
agregar_usuario("Fernando")

inscribir_usuario_en_cursos("Eduardo", ["Python Basico", "SqlAlchemy"])
inscribir_usuario_en_cursos("Fernando", ["Python Basico"])

mostrar_cursos_de_usuario("Eduardo")
mostrar_usuarios_de_curso("Python Basico")
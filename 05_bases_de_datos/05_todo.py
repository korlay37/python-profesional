import os
from datetime import datetime
from sqlalchemy import create_engine, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, Session

Base = declarative_base()
engine = create_engine("sqlite:///app.db")

class Tarea(Base):
    __tablename__ = "tareas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String, nullable=False)
    completada: Mapped[bool] = mapped_column(Boolean, default=False)
    creada: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    actualizada: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self) -> str:
        estado = "✅" if self.completada else "❌"
        creada = self.creada.strftime("%Y-%m-%d %H:%M")
        actualizada = self.actualizada.strftime("%Y-%m-%d %H:%M")
        return f"[{self.id}] {self.titulo} - {estado} (Creada: {creada} | Actualizada: {actualizada})"

Base.metadata.create_all(engine)

def crear_tarea(titulo:str) -> None:
    titulo = titulo.strip()
    if not titulo:
        print("El titulo no puede estar vacio")
        return
    with Session(engine) as session:
        tarea: Tarea = Tarea(titulo=titulo)
        session.add(tarea)
        try:
            session.commit()
            print("Tarea creada")
        except Exception as e:
            session.rollback()
            print("Error al crear tarea")

def ver_tareas() -> None:
    with Session(engine) as session:
        tareas = session.query(Tarea).all()
        if tareas:
            print("Lista de tareas: ")
            for tarea in tareas:
                print(f"    {tarea}")
        else:
            print("No hay tareas")

def marcar_completada(tarea_id: int, completada: bool) -> None:
    with Session(engine) as session:
        tarea = session.get(Tarea, tarea_id)
        if tarea:
            tarea.completada = completada
            try:
                session.commit()
                print("Tarea actualizada")
            except Exception as e:
                session.rollback()
                print(f"Error al actualizar tarea: {e}")
        else:
            print("Tarea no encontrada")

def borrar_tarea(tarea_id: int) -> None:
    with Session(engine) as session:
        tarea = session.get(Tarea, tarea_id)
        if tarea:
            session.delete(tarea)
            session.commit()
            print("Tarea eliminada")
        else:
            print("Tarea no encontrada")

# Parte 3
# Crea menu() -> None
#   - While infinito
#   - Borra pantalla
#   - Imprime las opciones:
#       print("\n Menú de tareas:")
#       print("1. Crear tarea")
#       print("2. Ver tareas")
#       print("3. Marcar como completada")
#       print("4. Borrar tarea")
#       print("5. Salir")
# Recibe la opcion
# Borra pantalla
# Implementa el codigo para cada opcion
# NOTA para que funcione el borrar la pantalla antes del menu,
# puedes poner un input("\nPresiona enter para continuar...")
# para pausar la ejecucion del codigo antes de borrar pantalla.

def menu() -> None:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n Menú de tareas:")
        print("1. Crear tarea")
        print("2. Ver tareas")
        print("3. Marcar como completada")
        print("4. Borrar tarea")
        print("5. Salir")

        opcion: str = input("Elige una opcion: ")
        os.system("cls" if os.name == "nt" else "clear")

        if opcion == "1":
            titulo:str = input("Titulo: ")
            crear_tarea(titulo)
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            ver_tareas()
            try:
                tarea_id: int = int(input("ID de la tarea a marcar completada: "))
                marcar_completada(tarea_id, True)
            except ValueError:
                print("ID invalido")
        elif opcion == "4":
            ver_tareas()
            try:
                tarea_id: int = int(input("ID de la tarea a eliminar: "))
                borrar_tarea(tarea_id)
            except ValueError:
                print("ID invalido")
        elif opcion == "5":
            break
        else:
            print("Opcion invalida")
        input("\nPresiona ENTER para continuar...")

if __name__ == "__main__":
    menu()

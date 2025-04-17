
import sqlite3

conn: sqlite3.Connection = sqlite3.connect("usuarios.db")

cursor: sqlite3.Cursor = conn.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

conn.commit()

# Crear un usuario
def insertar_usuario(nombre: str, edad: int) -> None:
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (nombre, edad))
    conn.commit()

# insertar_usuario("Ana", 30)
# insertar_usuario("Luis", 25)

# Consultar usuario
def obtener_usuarios() -> list:
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# for usuario in obtener_usuarios():
#     print(usuario)

# Eliminar usuario
def eliminar_usuario_por_id(user_id: int) -> None:
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

eliminar_usuario_por_id(1)
for usuario in obtener_usuarios():
    print(usuario)

conn.close()
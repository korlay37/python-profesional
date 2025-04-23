import sqlite3

def guardar_usuario(nombre: str, edad: int) -> None:
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conn.commit()
    conn.close()
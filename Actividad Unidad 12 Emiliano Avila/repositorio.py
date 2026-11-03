import os
import sqlite3

CARPETA = os.path.dirname(os.path.abspath(__file__))
NOMBRE_DB = os.path.join(CARPETA, "biblioteca.db")

def conectar():
    conexion = sqlite3.connect(NOMBRE_DB)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

def inicializar_bd():
    """Crea las tablas si no existen (misma estructura que el TP anterior)."""
    conexion = conectar()
    try:
        conexion.execute("""
            CREATE TABLE IF NOT EXISTS autores (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre       TEXT NOT NULL,
                nacionalidad TEXT
            )
        """)
        conexion.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                id       INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo   TEXT NOT NULL,
                anio     INTEGER,
                autor_id INTEGER NOT NULL,
                FOREIGN KEY (autor_id) REFERENCES autores(id)
            )
        """)
        conexion.commit()
    finally:
        conexion.close()

def obtener_autores_db():
    conexion = conectar()
    try:
        filas = conexion.execute("SELECT id, nombre, nacionalidad FROM autores").fetchall()
        return [dict(fila) for fila in filas]
    finally:
        conexion.close()

def obtener_autor_db(id):
    conexion = conectar()
    try:
        fila = conexion.execute(
            "SELECT id, nombre, nacionalidad FROM autores WHERE id = ?", (id,)
        ).fetchone()
        return dict(fila) if fila else None
    finally:
        conexion.close()

def insertar_autor_db(nombre, nacionalidad):
    """Inserta un autor y devuelve el ID generado."""
    conexion = conectar()
    try:
        cursor = conexion.execute(
            "INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)",
            (nombre, nacionalidad),
        )
        conexion.commit()
        return cursor.lastrowid
    finally:
        conexion.close()

CONSULTA_LIBROS = """
    SELECT libros.id, libros.titulo, libros.anio, libros.autor_id,
           autores.nombre AS autor_nombre,
           autores.nacionalidad AS autor_nacionalidad
    FROM libros
    JOIN autores ON libros.autor_id = autores.id
"""

def _armar_libro(fila):
    """Convierte una fila del JOIN en un diccionario con el autor anidado."""
    return {
        "id": fila["id"],
        "titulo": fila["titulo"],
        "anio": fila["anio"],
        "autor": {
            "id": fila["autor_id"],
            "nombre": fila["autor_nombre"],
            "nacionalidad": fila["autor_nacionalidad"],
        },
    }

def obtener_libros_db():
    conexion = conectar()
    try:
        filas = conexion.execute(CONSULTA_LIBROS + " ORDER BY libros.id").fetchall()
        return [_armar_libro(fila) for fila in filas]
    finally:
        conexion.close()

def obtener_libro_db(id):
    conexion = conectar()
    try:
        fila = conexion.execute(CONSULTA_LIBROS + " WHERE libros.id = ?", (id,)).fetchone()
        return _armar_libro(fila) if fila else None
    finally:
        conexion.close()

def insertar_libro_db(titulo, anio, autor_id):
    """Inserta un libro y devuelve su ID."""
    conexion = conectar()
    try:
        cursor = conexion.execute(
            "INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)",
            (titulo, anio, autor_id),
        )
        conexion.commit()
        return cursor.lastrowid
    finally:
        conexion.close()

def actualizar_libro_db(id, titulo, anio, autor_id):
    """Actualiza un libro. Devuelve True si existía, False si no."""
    conexion = conectar()
    try:
        cursor = conexion.execute(
            "UPDATE libros SET titulo = ?, anio = ?, autor_id = ? WHERE id = ?",
            (titulo, anio, autor_id, id),
        )
        conexion.commit()
        return cursor.rowcount > 0
    finally:
        conexion.close()

def eliminar_libro_db(id):
    """Elimina un libro. Devuelve True si existía, False si no."""
    conexion = conectar()
    try:
        cursor = conexion.execute("DELETE FROM libros WHERE id = ?", (id,))
        conexion.commit()
        return cursor.rowcount > 0
    finally:
        conexion.close()
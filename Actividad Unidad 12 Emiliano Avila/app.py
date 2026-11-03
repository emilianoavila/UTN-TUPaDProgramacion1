"""
API REST de Biblioteca con Flask + SQLite
UTN Mendoza - Programación

Ejecutar con:  python app.py
La API queda en: http://127.0.0.1:5000
"""

from flask import Flask, jsonify, request

import repositorio as repo

app = Flask(__name__)
app.json.ensure_ascii = False

repo.inicializar_bd()

def error(mensaje, codigo):
    """Devuelve una respuesta de error en formato JSON."""
    return jsonify({"error": mensaje}), codigo

def es_entero(valor):
    """True si es un int (en Python, bool también es int, así que lo excluyo)."""
    return isinstance(valor, int) and not isinstance(valor, bool)

def es_texto_valido(valor):
    return isinstance(valor, str) and valor.strip() != ""

def leer_json():
    """Devuelve el cuerpo JSON como diccionario, o None si es inválido."""
    datos = request.get_json(silent=True)
    if not isinstance(datos, dict):
        return None
    return datos

@app.route("/api/autores", methods=["GET"])
def listar_autores():
    return jsonify(repo.obtener_autores_db()), 200

@app.route("/api/autores", methods=["POST"])
def crear_autor():
    datos = leer_json()
    if datos is None:
        return error("El cuerpo de la petición debe ser un JSON válido.", 400)

    faltantes = [c for c in ("nombre", "nacionalidad") if c not in datos]
    if faltantes:
        return error(f"Faltan campos obligatorios: {', '.join(faltantes)}.", 400)

    if not es_texto_valido(datos["nombre"]) or not es_texto_valido(datos["nacionalidad"]):
        return error("'nombre' y 'nacionalidad' deben ser texto no vacío.", 400)

    nuevo_id = repo.insertar_autor_db(datos["nombre"].strip(), datos["nacionalidad"].strip())
    return jsonify(repo.obtener_autor_db(nuevo_id)), 201

@app.route("/api/libros", methods=["GET"])
def listar_libros():
    return jsonify(repo.obtener_libros_db()), 200

@app.route("/api/libros/<int:id>", methods=["GET"])
def obtener_libro(id):
    libro = repo.obtener_libro_db(id)
    if libro is None:
        return error(f"No existe un libro con id {id}.", 404)
    return jsonify(libro), 200

@app.route("/api/libros", methods=["POST"])
def crear_libro():
    datos = leer_json()
    if datos is None:
        return error("El cuerpo de la petición debe ser un JSON válido.", 400)

    faltantes = [c for c in ("titulo", "anio", "autor_id") if c not in datos]
    if faltantes:
        return error(f"Faltan campos obligatorios: {', '.join(faltantes)}.", 400)

    if not es_texto_valido(datos["titulo"]):
        return error("'titulo' debe ser texto no vacío.", 400)
    if not es_entero(datos["anio"]):
        return error("'anio' debe ser un número entero.", 400)
    if not es_entero(datos["autor_id"]):
        return error("'autor_id' debe ser un número entero.", 400)

    if repo.obtener_autor_db(datos["autor_id"]) is None:
        return error(f"No existe un autor con id {datos['autor_id']}.", 404)

    nuevo_id = repo.insertar_libro_db(datos["titulo"].strip(), datos["anio"], datos["autor_id"])
    return jsonify(repo.obtener_libro_db(nuevo_id)), 201

@app.route("/api/libros/<int:id>", methods=["PUT"])
def actualizar_libro(id):
    actual = repo.obtener_libro_db(id)
    if actual is None:
        return error(f"No existe un libro con id {id}.", 404)

    datos = leer_json()
    if datos is None:
        return error("El cuerpo de la petición debe ser un JSON válido.", 400)

    campos = [c for c in ("titulo", "anio", "autor_id") if c in datos]
    if not campos:
        return error("Debe enviar al menos un campo a modificar: titulo, anio o autor_id.", 400)

    # Parto de los valores actuales y piso solo los que llegaron
    titulo = actual["titulo"]
    anio = actual["anio"]
    autor_id = actual["autor"]["id"]

    if "titulo" in datos:
        if not es_texto_valido(datos["titulo"]):
            return error("'titulo' debe ser texto no vacío.", 400)
        titulo = datos["titulo"].strip()

    if "anio" in datos:
        if not es_entero(datos["anio"]):
            return error("'anio' debe ser un número entero.", 400)
        anio = datos["anio"]

    if "autor_id" in datos:
        if not es_entero(datos["autor_id"]):
            return error("'autor_id' debe ser un número entero.", 400)
        if repo.obtener_autor_db(datos["autor_id"]) is None:
            return error(f"No existe un autor con id {datos['autor_id']}.", 404)
        autor_id = datos["autor_id"]

    repo.actualizar_libro_db(id, titulo, anio, autor_id)
    return jsonify(repo.obtener_libro_db(id)), 200

@app.route("/api/libros/<int:id>", methods=["DELETE"])
def eliminar_libro(id):
    if not repo.eliminar_libro_db(id):
        return error(f"No existe un libro con id {id}.", 404)
    return jsonify({"mensaje": f"Libro {id} eliminado correctamente."}), 200

@app.errorhandler(404)
def no_encontrado(e):
    return error("Recurso no encontrado.", 404)

@app.errorhandler(405)
def metodo_no_permitido(e):
    return error("Método HTTP no permitido para esta ruta.", 405)

@app.errorhandler(500)
def error_interno(e):
    return error("Error interno del servidor.", 500)

if __name__ == "__main__":
    app.run(debug=True)
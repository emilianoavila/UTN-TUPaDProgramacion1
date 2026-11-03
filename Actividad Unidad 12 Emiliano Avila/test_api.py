"""
Script de prueba automática de la API (usa la librería requests).

Pasos:
  1) Abrir una terminal y ejecutar:   python app.py
  2) En OTRA terminal ejecutar:       python test_api.py
"""

import requests

BASE_URL = "http://127.0.0.1:5000/api"


def mostrar(titulo, respuesta):
    print(f"\n--- {titulo} ---")
    print("Código:", respuesta.status_code)
    print("Respuesta:", respuesta.json())


def main():
    # 1) GET /api/libros
    r = requests.get(f"{BASE_URL}/libros", timeout=5)
    mostrar("1) GET /api/libros", r)
    assert r.status_code == 200

    # 2) POST autor y luego libro
    r = requests.post(
        f"{BASE_URL}/autores",
        json={"nombre": "Julio Cortázar", "nacionalidad": "Argentina"},
        timeout=5,
    )
    mostrar("2a) POST /api/autores", r)
    assert r.status_code == 201
    autor_id = r.json()["id"]

    r = requests.post(
        f"{BASE_URL}/libros",
        json={"titulo": "Rayuela", "anio": 1963, "autor_id": autor_id},
        timeout=5,
    )
    mostrar("2b) POST /api/libros", r)
    assert r.status_code == 201
    libro_id = r.json()["id"]

    # 3) PUT: actualizar el título del libro recién creado
    r = requests.put(
        f"{BASE_URL}/libros/{libro_id}",
        json={"titulo": "Rayuela (Edición especial)"},
        timeout=5,
    )
    mostrar("3) PUT /api/libros/<id>", r)
    assert r.status_code == 200
    assert r.json()["titulo"] == "Rayuela (Edición especial)"

    # 4) DELETE: eliminar el libro y verificar
    r = requests.delete(f"{BASE_URL}/libros/{libro_id}", timeout=5)
    mostrar("4a) DELETE /api/libros/<id>", r)
    assert r.status_code == 200

    r = requests.get(f"{BASE_URL}/libros/{libro_id}", timeout=5)
    mostrar("4b) Verificación: GET del libro eliminado (debe dar 404)", r)
    assert r.status_code == 404

    # Extra: validación de errores
    r = requests.post(f"{BASE_URL}/libros", json={"titulo": "Sin datos"}, timeout=5)
    mostrar("Extra) POST con campos faltantes (debe dar 400)", r)
    assert r.status_code == 400

    print("\n✔ Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("No se pudo conectar con la API. ¿Ejecutaste 'python app.py' primero?")
    except AssertionError:
        print("\n✘ Una de las pruebas falló. Revisá la respuesta mostrada arriba.")

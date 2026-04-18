from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

# app/app.py

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Maneja la ruta principal de la aplicación web.

    Soporta métodos GET y POST:
    - GET: Renderiza la página inicial sin resultado.
    - POST: Procesa los datos enviados desde el formulario para realizar
      una operación matemática básica.

    Parámetros esperados en el formulario (request.form):
    - num1 (str): Primer número, convertible a float.
    - num2 (str): Segundo número, convertible a float.
    - operacion (str): Tipo de operación a realizar. Puede ser:
        - "sumar"
        - "restar"
        - "multiplicar"
        - "dividir"

    Retorna:
        Response: Renderiza la plantilla 'index.html' con el resultado de la operación
        o un mensaje de error si ocurre alguna excepción.
    """
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":  # pragma: no cover
    # Quita debug=True para producción
    app.run(debug=True, port=5000, host="0.0.0.0")

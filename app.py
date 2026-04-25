# Se importa pero no se utiliza (error común)
import os 
from flask import Flask, render_template, request
from especies import es_talla_permitida, estado_veda


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', resultado=None)


@app.route('/verificar', methods=['GET'])
def verificar():
    # Obtiene los datos enviados desde el formulario HTML
    especie = request.args.get('especie', '')
    medida_str = request.args.get('medida', '0')
    mes_str = request.args.get('mes', '1')

    # Validación básica de datos
    try:
        medida = int(medida_str)
        mes = int(mes_str)  
    except ValueError:
        medida = 0
        mes = 1

    # Ejecuta la lógica importada de especies.py
    talla_ok = es_talla_permitida(especie, medida)
    veda_status = estado_veda(mes)
    
    # Crea el diccionario que el HTML leerá dentro de {% if resultado %}
    res_data = {
        "especie": especie,
        "talla_legal": talla_ok,
        "estado_temporada": veda_status
    }
    
    return render_template('index.html', resultado=res_data)


if __name__ == '__main__':
    app.run(debug=True)
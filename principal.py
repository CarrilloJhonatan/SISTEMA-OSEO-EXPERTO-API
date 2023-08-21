# Importar módulos y clases necesarias
from random import choice
from flask import Flask, request, jsonify
from sistemadereglas import *
import json
import datetime

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Inicializar el motor de reglas y las estructuras de datos para almacenar registros y diagnósticos
engine = SistemaOseoEngine()
registros = []
usuarios_diagnosticos = {}

# Definir una ruta para recibir datos de diagnóstico mediante una solicitud POST
@app.route('/diagnostico', methods=['POST'])
def obtener_diagnostico():
    # Obtener los datos del cuerpo de la solicitud JSON
    data = request.json
    usuario = data.get('usuario')

    # Extraer las respuestas del usuario de los datos
    lugar_del_dolor = data.get('lugar_del_dolor')
    duracion_del_dolor = data.get('duracion_del_dolor')
    tipo_de_dolor = data.get('tipo_de_dolor')
    sintomas_adicionales = data.get('sintomas_adicionales')
    historial_medico = data.get('historial_medico')

    # Inicializar o actualizar el registro de diagnósticos del usuario
    if usuario not in usuarios_diagnosticos:
        usuarios_diagnosticos[usuario] = []

    # Resetear el motor de reglas y declarar las respuestas como hechos
    engine.reset()
    engine.declare(reglas(lugar_del_dolor=lugar_del_dolor,
                          duracion_del_dolor=duracion_del_dolor,
                          tipo_de_dolor=tipo_de_dolor,
                          sintomas_adicionales=sintomas_adicionales,
                          historial_medico=historial_medico))

    # Ejecutar el motor de reglas para obtener diagnósticos
    engine.run()

    # Obtener los diagnósticos del motor y agregarlos al registro del usuario
    diagnostico = engine.obtener_diagnosticos()
    usuarios_diagnosticos[usuario].extend(diagnostico)

    # Crear un registro con los datos del usuario, respuestas y diagnósticos
    registro = {
        "usuario": usuario,
        "respuestas": {
            "lugar_del_dolor": lugar_del_dolor,
            "duracion_del_dolor": duracion_del_dolor,
            "tipo_de_dolor": tipo_de_dolor,
            "sintomas_adicionales": sintomas_adicionales,
            "historial_medico": historial_medico
        },
        "diagnostico": diagnostico,
        "fecha_registro": str(datetime.datetime.now())
    }

    # Agregar el registro a la lista de registros
    registros.append(registro)

    # Guardar los registros en un archivo JSON
    with open('registros.json', 'w') as json_file:
        json.dump(registros, json_file, indent=4)

    # Responder con los diagnósticos obtenidos en formato JSON
    return jsonify({'diagnostico': diagnostico})

# Definir una ruta para obtener todos los registros almacenados
@app.route('/resultados', methods=['GET'])
def mostrar_resultados():
    return jsonify({'registros': registros})

# Definir una ruta para buscar registros basados en un parámetro (nombre o DNI)
@app.route('/buscar/<parametro>', methods=['GET'])
def buscar_por_parametro(parametro):
    resultados_encontrados = []
    for registro in registros:
        if parametro.lower() in registro['usuario'].lower():
            resultados_encontrados.append(registro)
    return jsonify({'resultados_encontrados': resultados_encontrados})

# Iniciar la aplicación Flask si se ejecuta directamente (no se importa como módulo)
if __name__ == '__main__':
    app.run(debug=True)
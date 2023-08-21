# Importar módulos y clases necesarias
from random import choice
from flask import Flask, request, jsonify
from sistemadereglas import *
import json
import datetime

# Definición de la clase SistemaDiagnostico
class SistemaDiagnostico:
    def __init__(self):
        # Crear una instancia de Flask y otras variables para el sistema
        self.app = Flask(__name__)
        self.engine = SistemaOseoEngine()
        self.registros = []
        self.usuarios_diagnosticos = {}

        # Definir rutas para las funciones usando el decorador route
        self.app.route('/diagnostico', methods=['POST'])(self.obtener_diagnostico)
        self.app.route('/resultados', methods=['GET'])(self.mostrar_resultados)
        self.app.route('/buscar/<parametro>', methods=['GET'])(self.buscar_por_parametro)

    def run(self):
        # Iniciar la aplicación Flask con el modo de depuración habilitado
        self.app.run(debug=True)

    def obtener_diagnostico(self):
        # Obtener datos de la solicitud JSON
        data = request.json

        # Extraer el campo de usuario de los datos
        usuario = data.get('usuario')

        # Verificar si el campo de usuario está vacío y responder con un error 400 si es así
        if not usuario:
            return jsonify({'error': 'El campo "usuario" es obligatorio'}), 400

        # Extraer otras respuestas del usuario de los datos
        lugar_del_dolor = data.get('lugar_del_dolor')
        duracion_del_dolor = data.get('duracion_del_dolor')
        tipo_de_dolor = data.get('tipo_de_dolor')
        sintomas_adicionales = data.get('sintomas_adicionales')
        historial_medico = data.get('historial_medico')

        # Inicializar o actualizar el registro de diagnósticos del usuario
        if usuario not in self.usuarios_diagnosticos:
            self.usuarios_diagnosticos[usuario] = []

        # Resetear el motor de reglas y declarar las respuestas como hechos
        self.engine.reset()
        self.engine.declare(reglas(
            lugar_del_dolor=lugar_del_dolor,
            duracion_del_dolor=duracion_del_dolor,
            tipo_de_dolor=tipo_de_dolor,
            sintomas_adicionales=sintomas_adicionales,
            historial_medico=historial_medico
        ))

        # Ejecutar el motor de reglas para obtener diagnósticos
        self.engine.run()
        diagnostico = self.engine.obtener_diagnosticos()

        # Agregar el diagnóstico obtenido al registro del usuario
        self.usuarios_diagnosticos[usuario].extend(diagnostico)

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
        self.registros.append(registro)

        # Guardar los registros en un archivo JSON
        with open('registros.json', 'w') as json_file:
            json.dump(self.registros, json_file, indent=4)

        # Responder con el diagnóstico obtenido en formato JSON
        return jsonify({'diagnostico': diagnostico})

    def mostrar_resultados(self):
        # Responder con todos los registros almacenados en formato JSON
        return jsonify({'registros': self.registros})

    def buscar_por_parametro(self, parametro):
        # Buscar registros basados en un parámetro (nombre o DNI)
        resultados_encontrados = []
        for registro in self.registros:
            if parametro.lower() in registro['usuario'].lower():
                resultados_encontrados.append(registro)
        # Responder con los registros encontrados en formato JSON
        return jsonify({'resultados_encontrados': resultados_encontrados})

# Iniciar la aplicación si se ejecuta directamente (no se importa como módulo)
if __name__ == '__main__':
    # Crear una instancia del SistemaDiagnostico y ejecutar la aplicación Flask
    sistema = SistemaDiagnostico()
    sistema.run()
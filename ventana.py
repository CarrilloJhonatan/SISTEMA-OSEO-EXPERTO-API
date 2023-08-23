# Importar las bibliotecas necesarias
import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow
from sistema_oseo_ui import Ui_MainWindow  # Importar la clase de la UI generada

# Crear una clase para la ventana principal de la aplicación
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Crear una instancia de la clase de la UI
        self.ui.setupUi(self)  # Configurar la disposición de la UI

        # Conectar los eventos de clic de los botones a sus respectivas funciones
        self.ui.onClickBuscar.clicked.connect(self.mostrar_resultados)
        self.ui.enviarDatos.clicked.connect(self.enviar_datos)

    # Función para mostrar los resultados de búsqueda según la entrada del usuario
    def mostrar_resultados(self):
        try:
            nombre = self.ui.filtradoNombre.text()  # Obtener la entrada del cuadro de texto

            print(f"Filtrando por nombre: {nombre}")

            if not nombre:
                response = requests.get("http://localhost:5000/resultados")
            else:
                response = requests.get(f"http://localhost:5000/buscar/{nombre}")

            print(f"Respuesta de la API: {response.text}")

            self.ui.TextDiagnostico.setPlainText("No se encuentran registros.")

            data = response.json()

            if 'registros' in data or 'resultados_encontrados' in data:
                resultados_text = ""
                if 'registros' in data:
                    registros = data['registros']
                else:
                    registros = data['resultados_encontrados']

                for resultado in registros:
                    resultados_text += f"Usuario: {resultado['usuario']}\nDiagnóstico: {resultado['diagnostico']}\nFecha: {resultado['fecha_registro']}\n\n"
                self.ui.TextDiagnostico.setPlainText(resultados_text)

                if not resultados_text:
                    self.ui.TextDiagnostico.setPlainText("No se encuentra información.")
        except requests.RequestException as e:
            self.ui.TextDiagnostico.setPlainText("Error al conectar con la API Flask.")

    # Función para enviar los datos del usuario al servidor
    def enviar_datos(self):
        try:
            # Obtener los valores de los botones de opción
            diagnostico_1 = "si" if self.ui.radioButton_r1_1.isChecked() else "no"
            diagnostico_2 = "si" if self.ui.radioButton_r2_1.isChecked() else "no"
            diagnostico_3 = "si" if self.ui.radioButton_r3_1.isChecked() else "no"
            diagnostico_4 = "si" if self.ui.radioButton_r4_1.isChecked() else "no"
            diagnostico_5 = "si" if self.ui.radioButton_r5_1.isChecked() else "no"

            usuario = self.ui.inputpostuser.text()  # Obtener el texto del cuadro de entrada

            # Preparar los datos para enviar en la solicitud POST
            data = {
                "lugar_del_dolor": diagnostico_1,
                "sintomas_adicionales": diagnostico_2,
                "tipo_de_dolor": diagnostico_3,
                "duracion_del_dolor": diagnostico_4,
                "historial_medico": diagnostico_5,
                "usuario": usuario  
            }

            # Enviar una solicitud POST al servidor
            response = requests.post("http://localhost:5000/diagnostico", json=data)

            # Mostrar un mensaje de éxito o error según la respuesta
            if response.status_code == 200:
                self.ui.TextDiagnostico.setPlainText("¡Datos enviados correctamente!")
                self.limpiar_formulario()  # Llamar a la función para limpiar el formulario
            else:
                self.ui.TextDiagnostico.setPlainText("Error al enviar los datos, valide que esta llenando todos los campos.")

        except requests.RequestException as e:
            self.ui.TextDiagnostico.setPlainText("Error al conectar con la API Flask.")

    def limpiar_formulario(self):
        # Restablecer los valores predeterminados de los widgets
        self.ui.radioButton_r1_0.setChecked(False)
        self.ui.radioButton_r2_0.setChecked(False)
        self.ui.radioButton_r3_0.setChecked(False)
        self.ui.radioButton_r4_0.setChecked(False)
        self.ui.radioButton_r5_0.setChecked(False)
        self.ui.radioButton_r1_1.setChecked(False)
        self.ui.radioButton_r2_1.setChecked(False)
        self.ui.radioButton_r3_1.setChecked(False)
        self.ui.radioButton_r4_1.setChecked(False)
        self.ui.radioButton_r5_1.setChecked(False)
        self.ui.inputpostuser.clear()


# Iniciar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crear una instancia de la aplicación
    ventana = Ventana()  # Crear una instancia de la clase de la ventana principal
    ventana.show()  # Mostrar la ventana principal
    sys.exit(app.exec())  # Ejecutar el bucle de eventos de la aplicación
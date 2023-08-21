# Importar el módulo que contiene las reglas definidas
from reglas import *

# Definir una clase llamada "SistemaOseoEngine" que hereda de "KnowledgeEngine"
class SistemaOseoEngine(KnowledgeEngine):
    def __init__(self):
        super().__init__()  # Llamar al constructor de la clase base
        self.diagnosticos = []  # Inicializar el atributo "diagnosticos" como una lista vacía en el constructor

    # Definir un método llamado "obtener_diagnosticos" para obtener los diagnósticos recolectados
    def obtener_diagnosticos(self):
        diagnosticos = getattr(self, 'diagnosticos', [])  # Obtener los diagnósticos del atributo "diagnosticos"
        setattr(self, 'diagnosticos', [])  # Reiniciar la lista de diagnósticos para futuras ejecuciones
        return diagnosticos  # Retornar la lista de diagnósticos recolectados
#1
# Esta regla es ejecutada por el motor de reglas para agregar un diagnóstico a la lista de diagnósticos
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="NO")))
    def r1(self):
        self.diagnosticos.append("Sin Diagnóstico Específico")  # Agregar un diagnóstico a la lista
#2
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="SI")))
    def r2(self):
        self.diagnosticos.append("Enfermedad Preexistente")
#3
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="NO")))
    def r3(self):
        self.diagnosticos.append("Infección")
#4
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="SI")))
    def r4(self):
        self.diagnosticos.append("Infección")
# 5
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="NO")))
    def r5(self):
        self.diagnosticos.append('Inflamación o Irritación')
# 6
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="SI")))
    def r6(self):
        self.diagnosticos.append('Condición Crónica')
# 7
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="NO")))
    def r7(self):
        self.diagnosticos.append('Afección Aguda')
# 8
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="SI")))
    def r8(self):
        self.diagnosticos.append("Osteomielitis")
# 9
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="NO")))
    def r9(self):
        self.diagnosticos.append("Lesión Aguda")
# 10
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="SI")))
    def r10(self):
        self.diagnosticos.append("Fractura por Osteoporosis")
# 11
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="NO")))
    def r11(self):
        self.diagnosticos.append("Afección Aguda")
# 12
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="SI")))
    def r12(self):
        self.diagnosticos.append('Afección Crónica')
# 13
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="NO")))
    def r13(self):
        self.diagnosticos.append('Afección Inflamatoria')
# 14
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="SI")))
    def r14(self):
        self.diagnosticos.append('Enfermedad Crónica')
# 15
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="NO")))
    def r15(self):
        self.diagnosticos.append('Afección Inflamatoria')
# 16    
    @Rule(AND(reglas(lugar_del_dolor="NO")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="SI")))
    def r16(self):
        self.diagnosticos.append("Enfermedad Inflamatoria Aguda")
# 17
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="NO")))
    def r17(self):
        self.diagnosticos.append("Afección Localizada")
# 18
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="SI")))
    def r18(self):
        self.diagnosticos.append("Osteoartritis")
# 19
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="NO")))
    def r19(self):
        self.diagnosticos.append("Afección Inflamatoria Crónica")
# 20
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="SI")))
    def r20(self):
        self.diagnosticos.append('Condición Inflamatoria')
# 21
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="NO")))
    def r21(self):
        self.diagnosticos.append('Afección Crónica')
# 22
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="SI")))
    def r22(self):
        self.diagnosticos.append('Condición Preexistente')
# 23
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="NO")))
    def r23(self):
        self.diagnosticos.append("Artritis Reumatoide")
# 24
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="NO")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="SI")))
    def r24(self):
        self.diagnosticos.append("Condición Inflamatoria Crónica")
# 25
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="NO")))
    def r25(self):
        self.diagnosticos.append("Lesión Muscular")
# 26
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="SI")))
    def r26(self):
        self.diagnosticos.append("Condición Crónica")
# 27
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="NO")))
    def r27(self):
        self.diagnosticos.append('Lesión Aguda')
# 28
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="NO")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="SI")))
    def r28(self):
        self.diagnosticos.append('Enfermedad Inflamatoria Crónica')
# 29
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="NO")))
    def r29(self):
        self.diagnosticos.append('Lesión Aguda')
# 30
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="NO")), (reglas(historial_medico="SI")))
    def r30(self):
        self.diagnosticos.append('Condición Crónica')
# 31
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="NO")))
    def r31(self):
        self.diagnosticos.append('Enfermedad Inflamatoria')
# 32
    @Rule(AND(reglas(lugar_del_dolor="SI")), (reglas(duracion_del_dolor="SI")), (reglas(tipo_de_dolor="SI")), (reglas(sintomas_adicionales="SI")), (reglas(historial_medico="SI")))
    def r32(self):
        self.diagnosticos.append('Necesidad de Evaluación Médica Adicional')


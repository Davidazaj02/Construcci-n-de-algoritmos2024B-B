__author__ = "David Alejandro Aza Jojoa"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "david.azaj@campusucc.edu.co"

from Fecha import Fecha


class Empleado:
    # Aqui inicia la declaracion de mi clase
 
    '''#-----------------------------------------------------
    # Atributos
    -----------------------------------------------------#'''

    nombre=""
    apellido=""
    salario=""

    '''#------------------------------------------------------
    # 1 = Masculino, 2 = Femenino
    ------------------------------------------------------#'''
    sexo = 0

    '''#------------------------------------------------------
    # Asociacion 
    ------------------------------------------------------#'''

    fechaIngreso=Fecha()
    fechaNacimiento=Fecha()

    '''#---------------------------------------------------
    # Metodos
    ---------------------------------------------------#'''

    __method__ = ""
    __parameter__ = ""
    __returns__ = ""
    __Description__ = ""
    def DarNombre(self):
        # Aqui va mi codigo
        return self.nombre

    __method__ = ""
    __parameter__ = ""
    __returns__ = ""
    __Description__ = ""    
    def CambiarSalario(self, nuevoSalario):
        #Aqui va mi codigo
        self.salario = nuevoSalario


    __method__ = ""
    __parameter__ = ""
    __returns__ = ""
    __Description__ = ""
    def DarSalario(self):
        #Aqui va mi codigo
        return self.salario
    __method__ = ""
    __parameter__ = ""
    __returns__ = ""
    __Description__ = ""
    def ConsultarFechaIngreso(self):
        return self.fechaIngreso.DarFecha()
    
    __method__ = "CalcularSalarioAnual"
    __parameter__ = "ninguno"
    __returns__ = "Salario Anual"
    __Description__ = "Muestra el salario anual del empleado"
    def CalcularSalarioAnual(self):
        # Aqui va mi codigo
        # forma 1
        # total = self.salario*12
        # return total
        # forma 2
        return self.salario*12
    __method__ = "CalcularImpuestoSalarioAnual"
    __parameter__ = "ninguno"
    __returns__ = "Impuesto del Salario Anual"
    __Description__ = "Muestra el Impuesto del salario anual del empleado"
    def CalcularImpuestoSalarioAnual(self):
        # Aqui inicia mi codigo
        # Forma 1
        # SalarioAnual =self.CalcularImpuestoSalarioAnual()
        # ImpuestoAnual =SalarioAnual*0.19
        # forma 2
        return self.CalcularSalarioAnual()*0.19
    
    __method__ = "CalcularImpuestoSalarioAnual"
    __parameter__ = "ninguno"
    __returns__ = "Impuesto del Salario Anual"
    __Description__ = "Muestra el Impuesto del salario anual del empleado"
    def calcularImpuestoSalarioMensual(self):
        return self.calcularImpuestoSalarioMensual()*0.19/12
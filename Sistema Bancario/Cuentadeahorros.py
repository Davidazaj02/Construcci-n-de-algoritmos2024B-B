__author__= "David Alejandro Aza Jojoa"
__License__="GPL"
__Version__="1.0.0"
__Email__="david.azaj@campusucc.edu.co"

from SimuladorBancario import SimuladorBancario

class CuentadeAhorros:

# Aqui inicia la declaracion de la clase

    """----------------------------------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------------------------------"""
    saldo= 0
    interes_mensual = 0.6



    __method__ = ""
    __parameter__ = ""
    __returns__ = ""
    __Description__ = ""

    __method__ = "DarSaldo"
    __parameter__ = "Saldo"
    __returns__ = "Saldo"
    __Description__ = " metodo que transfiere valor a otra cuenta"
    def consignarValor(self, nuevoValor): 
        #Aqui va el codigo
        self.saldo = self.saldo + nuevoValor

    __method__ = "DarValor"
    __parameter__ = "ninguno"
    __returns__ = "Saldo de la cuenta"
    __Description__ = "metodo que muestra el saldo de la cuenta"
    def Darsaldo(self):
        #aqui va el codigo
        return self.saldo
    
    __method__ = "retirarValor"
    __parameter__ = "monto"
    __returns__ = "saldo"
    __Description__ = "metodo que permite retirar saldo de la cuenta"
    def RetirarValor(self, monto):
        #aqui va el codigo
        self.saldo = self.saldo-monto

    __method__ = "DarInteresMensual"
    __parameter__ = "Ninguno"
    __returns__ = "Interes"
    __Description__ = "metodo que muestra el interes de la cuenta"
    def DarInteresMensual(self):
        #Aqui va el codigo
        return self.interes
    
    __method__ = "actualizarSaldoPorMes"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo"
    __Description__ = "metodo que actualiza el saldo"
    def actualizarSaldoPorPasoMes(self):
        #Aqui va el codigo
        ""


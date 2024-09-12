__author__="David Alejandro Aza Jojoa"
__license__="GPL"
__version__="1.0.0"
__email__="david.azaj@campusucc.edu.co"

from SimuladorBancario import SimuladorBancario

class CuentaCorriente:

    #-----------------------------------------------------
    # Atributos
    #-----------------------------------------------------
    __Interes=0
    __Saldo=0

    #-----------------------------------------------------
    # Métodos
    #-----------------------------------------------------  
    __method__ = "DarSaldo"
    __parameter__ = "Ninguno"
    __return__ = "Saldo de la cuenta"
    __description__ = "Metodo que muestra el saldo de la cuenta"

    def Darsaldo(self):
        #aqui inicia mi codigo
        return self.__Saldo
    
    __method__ = "ConsignarSaldo"
    __parameter__ = "Monto"
    __return__ = "Ninguno"
    __description__ = "Metodo que Permite consignar un monto a la cuenta corriente"
    def ConsignarSaldo(self, monto):
        #aqui inicia mi codigo
        self.__saldo = self.__saldo+monto

    __method__ = "RetirarSaldo"
    __parameter__ = "Monto"
    __return__ = "Ninguno"
    __description__ = "Metodo que Permite retirar un monto a la cuenta"
    def RetirarSaldo(self, monto):
        #aqui inicia mi codigo
        self.__saldo = self.__saldo-monto

    

    
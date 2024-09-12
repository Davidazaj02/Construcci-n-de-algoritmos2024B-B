__author__="David Alejandro Aza Jojoa"
__license__="GPL"
__version__="1.0.0"
__email__="david.azaj@campusucc.edu.co"

from Fecha import Fecha
from Cuentadeahorros import CuentadeAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:

    #-----------------------------------------------------
    # Atributos
    #-----------------------------------------------------
    __cedula = ''
    __nombre = ''
    __mesActual = 0


    #-----------------------------------------------------
    # Asociaciones
    #-----------------------------------------------------
    __CuentadeAhorros=CuentadeAhorros()
    __CuentaCorriente=CuentaCorriente()
    __CDT=CDT()
    #-----------------------------------------------------
    # Métodos
    #-----------------------------------------------------    
    __method__ = "DarSaldo"
    __parameter__ = "Ninguno"
    __return__ = "Saldo de la cuenta"
    __description__ = ""



    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite depositar en la cuenta corriente"
    def DepositarCuenraCorriente(self, monto):
        # Aqui inicia mi codigo
        self.__CuentaCorriente.ConsignarSaldo(monto)

    __method__ = "CalcularSaldoTotal"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo total de todas las cuentas"
    __Description__ = "Metodo que permite calcular el saldo total actual en todas las cuentas"
    def ConsultarSaldoTotal(self):
        # Aqui inicia mi codigo
        # Metodo 1
        # total = self.__CuentaCorriente.Darsaldo()+self.__CuentadeAhorros.Darsaldo()
        # return total
        # Metodo 2
        return "El saldo total es:" + self.CuentadeAhorros.Darsaldo() + self.CuentaCorriente.Darsaldo()
    
    __method__ = "PasarAhorrosACorriente"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite pasar saldo de la cuenta de ahorros a la cuenta corriente"
    def PasarAhorrosACorriente(self):
        # Aqui inicia mi codigo
        saldoAhorros = self.__CuentadeAhorros.Darsaldo()
        self.__CuentadeAhorros.Retirarsaldo(saldoAhorros)
        self.__CuentaCorriente.ConsignarSaldo(saldoAhorros)
    
    __method__ = "Ahorrar"
    __parameter__ = "Monto"
    __returns__ = ""
    __Description__ = "Pasa de la cuenta corriente a la cuenta de ahorros el valor que se entrega como parámetro (suponiendo que hay suficientes fondos)"
    def ahorrar(self, monto):
        self.__CuentadeAhorros.RetirarValor(monto)
        self.__CuentaCorriente.ConsignarSaldo(monto)

    __method__ = "retirarAhorro"
    __parameter__ = "Monto"
    __returns__ = ""
    __Description__ = "Retira un valor dado de la cuenta de ahorros (suponiendo que hay suficientes fondos)"
    def retirarAhorro(self, monto):
        self.__CuentadeAhorros.RetirarValor(monto)

    __method__ = "retirarTodo"
    __parameter__ = ""
    __returns__ = ""
    __Description__ = "Retira todo el dinero que hay en la cuenta corriente y en la cuenta de ahorros" 
    def retirarTodo(self):
        self.__CuentaCorriente.RetirarSaldo(self.__CuentaCorriente.Darsaldo())
        self.__CuentadeAhorros.RetirarValor(self.__CuentadeAhorros.Darsaldo())

    __method__ = "duplicarAhorro"
    __parameter__ = ""
    __returns__ = ""
    __Description__ = "Duplica la cantidad de dinero que hay en la cuenta de ahorros"
    def duplicarAhorros(self):
        self.__CuentadeAhorros.consignarValor(self.__CuentadeAhorros.Darsaldo())

    __method__ = "DarSaldoCorriente"
    __parameter__ = ""
    __return__ = "saldo"
    __description__ = "Retorna el saldo que hay en la cuenta corriente. No olvide que éste es un método de la clase CuentaBancaria."

    def DarsaldoCorriente(self):
        #aqui inicia mi codigo
        return self.__CuentaCorriente.Darsaldo()
    
"""
Diseña una clase CuentaBancaria con los atributos titular,
saldo y moneda. Implementa
métodos para depositar dinero, retirar dinero
(validando que no se retire más de lo
disponible) y otro que muestre el saldo actual.
"""
class CuentaBancaria:
    def __init__(self, titular, saldo, moneda):
        self.titular = titular
        self.saldo = saldo
        self.moneda = moneda


    def deposito(self,deposito):

        if deposito != self.saldo:
            self.saldo = deposito + self.saldo
            return f"tu deposito es: {deposito}"


    def retirar(self, retiro):

        if retiro <= self.saldo:
            self.saldo = self.saldo - retiro
            return f"la cantida retirada: {retiro}"
        return f"saldo insuficiente"

    def muestra_saldo(self):
        return f"Titular: {self.titular}, Su Saldo: {self.saldo} {self.moneda}"

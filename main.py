from cuenta_bancaria_3 import CuentaBancaria

cuenta1 = CuentaBancaria("Alberto Montero", 100, "Dolares")

print(cuenta1.retirar(20))

print(cuenta1.deposito(800))
print()
print(cuenta1.muestra_saldo())
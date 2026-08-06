# 🏦 Banking System Engine — Núcleo POO en Python

> **Una implementación modular e intuitiva en Python que demuestra los principios de la Programación Orientada a Objetos (POO), mutación de estados y validación de lógica transaccional.**

---

## 🏛️ Visión General de la Arquitectura

Este proyecto implementa un modelo de dominio encapsulado que representa la entidad de una cuenta bancaria (`CuentaBancaria`). Destaca por la separación de responsabilidades, gestionando los estados del saldo interno a través de interacciones financieras básicas (depósitos y retiros) con validación de reglas de negocio.

+-------------------------------+
   |        CuentaBancaria         |
   +-------------------------------+
   | - titular: str                |
   | - saldo: float                |
   | - moneda: str                 |
   +-------------------------------+
   | + deposito(deposito): str     |
   | + retirar(retiro): str        |
   | + muestra_saldo(): str        |
   +-------------------------------+
                  ^
                  | Instancia y Ejecuta
   +-------------------------------+
   |            main.py            |
   +-------------------------------+

   ---

## 💻 Código Fuente

### 📂 `cuenta_bancaria_3.py` (Modelo de Dominio)

```python
class CuentaBancaria:
    def __init__(self, titular: str, saldo: float, moneda: str):
        self.titular = titular
        self.saldo = saldo
        self.moneda = moneda

    def deposito(self, deposito: float) -> str:
        if deposito != self.saldo:
            self.saldo = deposito + self.saldo
            return f"tu deposito es: {deposito}"

    def retirar(self, retiro: float) -> str:
        if retiro <= self.saldo:
            self.saldo = self.saldo - retiro
            return f"la cantida retirada: {retiro}"
        return "saldo insuficiente"

    def muestra_saldo(self) -> str:
        return f"Titular: {self.titular}, Su Saldo: {self.saldo} {self.moneda}"

from cuenta_bancaria_3 import CuentaBancaria

# Inicialización de la entidad con estado base
cuenta1 = CuentaBancaria("Alberto Montero", 100, "Dolares")

# Ejecución de retiro y validación de estado
print(cuenta1.retirar(20))

# Ejecución de transacción de depósito
print(cuenta1.deposito(800))
print()

# Consulta del estado actual de la cuenta
print(cuenta1.muestra_saldo())

la cantida retirada: 20
tu deposito es: 800

Titular: Alberto Montero, Su Saldo: 880 Dolares
Process finished with exit code 0


🛠️ Tecnologías y Entorno
Lenguaje: Python 3.x

Paradigma: Programación Orientada a Objetos (POO)

IDE: PyCharm

Control de Versiones: Git & GitHub

👨‍💻 Desarrollador
Desarrollado con ☕ y Python por Alberto Montero (@AlbertoDev28).


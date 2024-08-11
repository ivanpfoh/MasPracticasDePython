class CuentaBancaria:
    
    def __init__(self):
        self.__saldo = 0
        
    def depositar(self, deposito):
        self.__saldo += deposito
    
    def retirar(self, retiro):
        self.__saldo -= retiro
        
    def consultar(self):
        print(self.__saldo)
    

cliente = CuentaBancaria()
cliente.depositar(50)
cliente.consultar()

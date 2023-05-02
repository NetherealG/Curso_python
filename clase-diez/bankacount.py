from datetime import datetime

class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.blnc = balance
        self.trncs = []
#trnc = transaction , trncs=transactions, blnc = balance, trnc_type = transaction type
    def deposit(self, amount):
        self.blnc += amount
        self.trncs.append(('deposito', amount))

    def withdraw(self, amount):
        if self.blnc >= amount:
            self.blnc -= amount
            self.trncs.append(('Transferencia', amount))
        else:
            print('saldo insuficiente')

    def statement(self):
        print(f'Numero Cuenta: {self.account_number}')
        print(f'Nombre: {self.name}')
        print('\n')
        print(f'{"Mov#":<20} {"Tipo":<20} {"fecha transaccion":<20} {"monto":<20} {"saldo":<20}')
        print('----------------------------------------------------------------------------------')
        for trnc in self.trncs:
            date = datetime.today().strftime('%d-%m-%Y') 
            trnc_type = trnc[0]
            amount = trnc[1]
            if trnc_type == 'deposito':
                self.blnc += amount
            else:
                self.blnc -= amount
            print(f'{self.trncs.index(trnc)+1:<20} {trnc_type:<20} {date:<20} {amount:<20} {self.blnc:<20}')

# Crear una cuenta bancaria
my_account1 = BankAccount('2015---8', 'nicolas soto', 1000)
my_account2 = BankAccount('2067---4', 'roberto manfinfla',500)

# Hacer  movimientos
print('\n')

my_account1.deposit(500)
my_account2.withdraw(200)
my_account1.deposit(1000)

#  estado de cuenta
my_account1.statement()
print('\n')
my_account2.statement()

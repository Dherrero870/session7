from bankaccount import Bankaccount
numero_cuenta = (input("Introduzca su IBAN:"))
account = Bankaccount(numero_cuenta)
print (f"Hay {account.get_balance()}€ en tu cuenta")
funds = float(input("¿Cuánto dinero quieres añadir?"))
account.add_funds(funds)
print (f"Tras esta operación hay {account.get_balance()}€ en tu cuenta.")
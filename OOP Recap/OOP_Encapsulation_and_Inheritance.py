# Encapsulation

class BankAccount:
    def __init__(self, name, money):
        self._name = name
        self.__money = money
        # private & protected cannot be access from outside the class.
        # private cannot be inherited by child classes but protected can.

    def set_money(self, new_amount):
        if new_amount < 100:
            print("Invalid")
            return
        self.__money = new_amount

    def _get_money(self):
        entered_pin = input("enter pin")
        if entered_pin == "123":
            print(self.__money)
            return self.__money
        else:
            print("Auth Error")


musa_account = BankAccount('Musa', 100_000)
musa_account.set_money(500)
musa_account.get_money()



class SpecialAccount(BankAccount):
    pass

saim = SpecialAccount('Saim', '100')
print(saim._get_money())





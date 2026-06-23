from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self,currency="USD"):
        self.currency=currency
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def refund(self,amount):
        pass
    def _validate(self,amount):
        if amount<0:
            raise ValueError("Amount cannot be negative.")
        

class CreditCard(PaymentMethod):
    def pay(self,amount):
        self._validate(amount)
        print(f"Paid ${amount} {self.currency} using CreditCard")
    def refund(self, amount):
        self._validate(amount)
        print(f"Refunded {amount} {self.currency} to CreditCard")

class PayPal(PaymentMethod):
    def pay(self,amount):
        self._validate(amount)
        print(f"Paid ${amount} {self.currency} using PayPal")
    def refund(self, amount):
        self._validate(amount)
        print(f"Refunded {amount} {self.currency} to PayPal")

class Cash(PaymentMethod):
    def pay(self,amount):
        self._validate(amount)
        print(f"Paid ${amount} {self.currency} in cash")
    def refund(self, amount):
        self._validate(amount)
        print(f"Refunded {amount} {self.currency} in cash")

methods=[CreditCard(currency="USD"),PayPal(currency="EUR"),Cash("PKR")]
for m in methods:
    m.pay(100)
    m.refund(50)
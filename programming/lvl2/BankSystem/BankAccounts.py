from Customers import Customer
from typing import List
import datetime
import uuid
from enum import Enum


class BankErrors(Exception):
    pass


class InvalidAmountError(BankErrors):
    pass

class SelfTransferError(BankErrors):
    pass


def get_error():
    raise ValueError('Some error!')


class AccountType(Enum):
    DEBIT = 1
    CREDIT = 2


class BankOperation:
    def __init__(self, operation_type: str, customer_id: str, amount: float | int | None = None, description: str | None = None):
        self.operation_id = uuid.uuid4()
        self.operation_type = operation_type
        self.customer_id = customer_id
        self.amount = amount
        self.description = description
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return (f"{self.timestamp} | "
                f"{self.operation_id} | "
                f"{self.operation_type} | "
                f"{self.customer_id} | "
                f"{self.amount} | "
                f"{self.description}")


class BankAccountCustomer:

    def __init__(self, customer: Customer, account_type: AccountType = AccountType.DEBIT.value, balance: float = 0.0):
        self.account_id = uuid.uuid4()
        self.bank_customer = customer
        self.account_type = account_type
        self.balance: float | int = balance if balance >= 0.0 else get_error()
        self.history_operations: List[BankOperation] = []

        # Добавляем счёт к клиенту
        customer.add_account(self)
        # добавить инфу о записи операции
        self._record_operation(operation_type='INITIAL_DEPOSIT', customer_id=customer.id, amount=balance, description='Создание счёта.')

    def _record_operation(self, operation_type: str, customer_id: str, amount: float | int | None = None, description: str | None = None) -> None:
        """Записать информацию об операции"""
        operation = BankOperation(operation_type=operation_type, customer_id=customer_id, amount=amount, description=description)
        self.history_operations.append(operation)

    def deposit(self, amount: float | int) -> None:
        """Пополнить счёт аккаунта"""
        if isinstance(amount, str):
            raise ValueError('Не верный тип данных')
        if amount < 0:
            raise InvalidAmountError('Сумма должна быть больше нуля')
        self.balance += amount
        self._record_operation(operation_type='DEPOSIT', customer_id=self.bank_customer.id, amount=amount, description='Пополнение баланса')

    def withdraw(self, amount: float | int) -> bool:
        """Снять деньги со счёта"""
        if amount > self.balance:
            self._record_operation(operation_type='WITHDRAW', customer_id=self.bank_customer.id, amount=amount, description=f'Недостаточно средств для снятия {amount:.2f}. Доступно: {self.balance:.2f}')
            return False
        else:
            self.balance -= amount
            self._record_operation(operation_type='WITHDRAW', customer_id=self.bank_customer.id, amount=amount, description=f'Со счёта {self.bank_customer.id} снято {amount:.2f}. Баланс: {self.balance:.2f}')
            return True

    def get_balance(self) -> float | int:
        """Получить текущий баланс"""
        return self.balance

    def get_history(self) -> list:
        """Получить историю операций"""
        return self.history_operations.copy()

    def transfer(self, target_account, amount):
        """Перевод на другой счет"""
        return TransferManager.transfer(source_account=self, target_account=target_account, amount=amount)

    def __str__(self) -> str:
        return (f"Account {self.account_id} | {self.account_type.value} | "
                f"Balance: {self.balance:.2f} | Customer: {self.bank_customer.name}")


class TransferManager:

    @staticmethod
    def transfer(source_account: BankAccountCustomer, target_account: BankAccountCustomer, amount: float) -> bool:
        try:
            if amount <= 0:
                raise InvalidAmountError('Сумма перевода должна быть больше нуля. Перевод не возможен.')
            if source_account.balance < amount:
                raise f'Перевод не возможен, недостаточно денежных средств у {source_account.account_id}'

            if source_account.account_id == target_account.account_id:
                raise SelfTransferError('На данный момент перевод сам себе не доступен')

            source_account.balance -= amount
            target_account.balance += amount
            # timestamp = datetime.datetime.now()
            source_account._record_operation(operation_type='TRANSFER', customer_id=str(source_account.account_id), amount=amount,
                                             description=f'Перевод денежных средств от {source_account.account_id} на {target_account.account_id}')
            target_account._record_operation(operation_type='TRANSFER', customer_id=str(source_account.account_id), amount=amount,
                                             description=f'Перевод денежных средств от {source_account.account_id} на {target_account.account_id}')
            return True
        except BankErrors:
            return False


customer1 = Customer(name='Pavel', address='Moscow', email='pavel@gmail.com')
customer2 = Customer(name='Roman', address='Sochi', email='roman@gmail.com')

account1 = BankAccountCustomer(customer=customer1, balance=100)
account2 = BankAccountCustomer(customer=customer2)

print(account1.get_balance(), account2.get_history())

account1.transfer(target_account=account2, amount=90)

print(account1.get_balance(), account1.get_balance())
print(account2.get_balance(), account2.get_balance())

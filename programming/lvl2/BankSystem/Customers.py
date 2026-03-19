import uuid
from typing import List
from BankAccounts import BankAccountCustomer

class Customer:

    def __init__(self, name, email, address):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.address = address
        self._accounts: List[BankAccountCustomer] = []

    def add_account(self, account: BankAccountCustomer) -> None:
        """Добавление счёта клиенту"""
        self._accounts.append(account)
        print(f'Пользователь {self.name} добавил аккаунт - {account.account_id}')

    def get_total_balance_of_customer(self):
        total_sum = 0
        for account in self._accounts:
            total_sum += account.get_balance()
        print(f'Общая сумма на всех аккаунтах = {total_sum}')
        return total_sum
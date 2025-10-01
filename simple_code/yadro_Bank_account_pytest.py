import pytest
import uuid


def get_error():
    raise 'Error'


class Bank:

    def __init__(self):
        pass


class BankAccount(Bank):

    def __init__(self, bank_account: str, balance: float = 0.0):
        self.bank_account = bank_account
        self.balance = balance if balance >= 0.0 else get_error()
        super().__init__()

    def deposit(self, amount: float) -> None:
        if isinstance(amount, str):
            return self.balance
        if amount < 0:
            return self.balance
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if isinstance(amount, str):
            raise 'Bad type'
        if self.balance > amount:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        return self.balance


@pytest.fixture()
def create_account_0() -> BankAccount:
    return BankAccount(bank_account=f'test-{uuid.uuid4()}')


@pytest.fixture()
def create_account_with_balance() -> BankAccount:
    return BankAccount(bank_account=f'test-{uuid.uuid4()}', balance=1000.0)


@pytest.mark.parametrize('add_amount', [0, 1, 0.99, 99999999])
def test_bank_deposit_positive(create_account_with_balance, add_amount):
    account = create_account_with_balance
    current_balance = account.get_balance()
    account.deposit(amount=add_amount)
    assert account.get_balance() == current_balance + add_amount


@pytest.mark.parametrize('add_amount', [-1, 'add_amount'])
def test_bank_deposit_negative(create_account_with_balance, add_amount):
    account = create_account_with_balance
    current_balance = account.get_balance()
    account.deposit(amount=add_amount)
    assert account.get_balance() == current_balance

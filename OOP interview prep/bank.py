from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod
from dataclasses import dataclass

#You are building the core backend engine for a new retail bank. We need an object-oriented system that can handle different types of bank accounts, process transactions, and maintain a verifiable history of all account activity.

# Core Requirements:
# Account Management: The system must support opening basic Checking Accounts and Savings Accounts.
# Checking Accounts have a set overdraft limit (e.g., they can go negative up to $500).
# Savings Accounts cannot be overdrawn, but they accrue a specified interest rate which can be applied on demand.
# Transactions: Customers must be able to deposit money, withdraw money, and transfer money between any two accounts.
# Audit Trail: Every successful action (deposit, withdrawal, transfer) must generate a timestamped Transaction record. The account should be able to print a statement of its transaction history.
# Edge Cases & Error Handling to Consider (Your interviewer will look for these):
# What happens if a user tries to withdraw more than their balance (and overdraft limit)?
# How do you handle a transfer where the withdrawal succeeds, but the deposit to the receiving account fails?
# How are you protecting the account balance from being modified directly from outside the class?

from datetime import datetime

from dataclasses import field


class BankError(Exception):
    """Base class for all banking-related errors."""


class InvalidAmountError(BankError):
    """Raised when a transaction amount is not positive."""


class InsufficientFundsError(BankError):
    """Raised when a withdrawal would exceed the available funds/overdraft."""


@dataclass
class Transaction:
    transaction_type: str
    amount: float
    balance_after: float
    timestamp: datetime = field(default_factory=datetime.now)

class Account (ABC):
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self._account_number = account_number
        self._balance = initial_balance
        self._transaction_history: List[Transaction] = []

    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError(f"Deposit amount must be positive, got {amount}")
        self.__record_deposit(amount, "DEPOSIT")

    def __record_deposit(self, amount: float, transaction_type: str) -> None:
        self._balance += amount
        self._transaction_history.append(Transaction(transaction_type, amount, self._balance))

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    def transfer(self, target_account: Account, amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError(f"Transfer amount must be positive, got {amount}")
        self.withdraw(amount)
        try:
            # Name mangling lets transfer reach this helper on another Account
            # instance, while keeping it out of the public/casual-access API.
            target_account.__record_deposit(amount, "TRANSFER_IN")
        except BankError:
            self.deposit(amount)  # rollback
            raise
        self._transaction_history.append(Transaction("TRANSFER_OUT", amount, self._balance))

    def get_transaction_history(self) -> List[Transaction]:
        return self._transaction_history.copy()

class Checking (Account):
    def __init__(self, account_number: str, initial_balance: float = 0.0, overdraft_limit: float = 500.0):
        super().__init__(account_number, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError(f"Withdrawal amount must be positive, got {amount}")
        if self._balance - amount < -self.overdraft_limit:
            raise InsufficientFundsError(
                f"Withdrawal of {amount} exceeds overdraft limit "
                f"(balance {self._balance}, overdraft limit {self.overdraft_limit})"
            )
        self._balance -= amount
        self._transaction_history.append(Transaction("WITHDRAWAL", amount, self._balance))

class Savings (Account):
    def __init__(self, account_number: str, initial_balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError(f"Withdrawal amount must be positive, got {amount}")
        if self._balance < amount:
            raise InsufficientFundsError(
                f"Withdrawal of {amount} exceeds balance {self._balance}"
            )
        self._balance -= amount
        self._transaction_history.append(Transaction("WITHDRAWAL", amount, self._balance))

    def add_interest(self) -> None:
        if self._balance <= 0:
            raise InvalidAmountError(
                f"Interest can only be applied to a positive balance, got {self._balance}"
            )
        interest = self._balance * self.interest_rate
        self._balance += interest
        self._transaction_history.append(Transaction("INTEREST", interest, self._balance))

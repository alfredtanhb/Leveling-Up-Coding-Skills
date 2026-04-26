class Account:
    """A simple class to represent a bank account."""

    def __init__(self, account_number: str, account_holder: str, balance: float) -> None:
        """Initialize the account with account number, holder name, and balance."""
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = max(0.0, balance)  # Ensure balance is non-negative

    def deposit(self, amount: float) -> bool:
        """Deposit money into the account. Returns True if successful, False otherwise."""
        if amount > 0:
            self.balance += amount
            print(f'${amount:.2f} deposited. New Balance: ${self.balance:.2f}')
            return True
        print('Error: Deposited amount must be greater than zero.')
        return False

    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the account. Returns True if successful, False otherwise."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'${amount:.2f} withdrawn. New Balance: ${self.balance:.2f}')
            return True
        print('Error: Inadequate funds in account.')
        return False

    def display(self) -> None:
        """Display the account details."""
        print(
            f'Account Number: {self.account_number}\n'
            f'Account Holder: {self.account_holder}\n'
            f'Balance: ${self.balance:.2f}'
        )

class SavingsAccount(Account):
    """A savings account with an interest rate."""

    def __init__(self, account_number: str, account_holder: str, balance: float, interest_rate: float) -> None:
        """Initialize the savings account with an interest rate."""
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = max(0.0, interest_rate)  # Ensure interest rate is non-negative

    def add_interest(self) -> bool:
        """Add interest to the savings account. Returns True if successful, False otherwise."""
        if self.interest_rate > 0:
            interest = self.balance * self.interest_rate / 100
            self.balance += interest
            print(f'Interest added: ${interest:.2f}. New Balance: ${self.balance:.2f}')
            return True
        print('Error: Interest rate must be greater than zero.')
        return False

    def display(self) -> None:
        """Display the savings account details, including the interest rate."""
        print(
            f'Savings Account Number: {self.account_number}\n'
            f'Savings Account Holder: {self.account_holder}\n'
            f'Savings Account Balance: ${self.balance:.2f}\n'
            f'Interest Rate: {self.interest_rate:.2f}%'
        )

class CurrentAccount(Account):
    """A current account with an overdraft limit."""

    def __init__(self, account_number: str, account_holder: str, balance: float, overdraft_limit: float) -> None:
        """Initialize the current account with an overdraft limit."""
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = max(0.0, overdraft_limit)  # Ensure overdraft limit is non-negative

    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the current account, considering the overdraft limit. Returns True if successful, False otherwise."""
        if amount > 0 and amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f'${amount:.2f} withdrawn. New Balance: ${self.balance:.2f}')
            return True
        print('Error: Overdraft limit exceeded.')
        return False

    def display(self) -> None:
        """Display the current account details, including the overdraft limit."""
        print(
            f'Current Account Number: {self.account_number}\n'
            f'Current Account Holder: {self.account_holder}\n'
            f'Current Account Balance: ${self.balance:.2f}\n'
            f'Overdraft Limit: ${self.overdraft_limit:.2f}'
        )
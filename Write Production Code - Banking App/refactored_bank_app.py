from abc import ABC, abstractmethod

## DECORATOR 
def transaction_logger(func):
    def wrapper(self, amount):
        print(f"[LOG] {func.__name__.upper()} of {amount} initiated")
        result = func(self, amount)
        print(f"[LOG] Transaction completed successfully\n")
        return result
    return wrapper

## ABSTRACT CLASS (Abstraction)
class Account(ABC):
    def __init__(self, account_number, account_holder, balance):
        """Initialize the account with account number, holder name, and balance."""
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = balance 

    @staticmethod
    def validate_amount(amount):
        return amount > 0
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self._balance += amount
            print(f'${amount:.2f} deposited. New Balance: ${self._balance:.2f}')
        else:
            print('Error: Deposited amount must be greater than zero.')
    
    @abstractmethod
    def withdraw(self, amount):
        """Withdraw money from the account"""
        pass

    @abstractmethod
    def display(self):
        """Display the account details."""
        pass


## LOAN APPLICATION (MULTIPLE INHERITANCE)
class LoanApplication:
    def apply_loan(self, amount):
        print(f"Loan of {amount} approved for {self.account_holder}")


## SAVINGS ACCOUNT (INHERITANCE)
class SavingsAccount(Account):
    """A savings account with an interest rate."""
    def __init__(self, account_number, account_holder, balance, interest_rate):
        """Initialize the savings account with an interest rate."""
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    @transaction_logger
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f'${amount:.2f} withdrawn. New Balance: ${self._balance:.2f}')
        else:
            print('Error: Inadequate funds in account.')
        
    def add_interest(self):
        """Add interest to the savings account"""
        interest = self._balance * self.interest_rate / 100
        self._balance += interest
        print(f'Interest added: ${interest:.2f}. New Balance: ${self._balance:.2f}')
        
    def display(self):
        """Display the savings account details, including the interest rate."""
        print(
            f'Savings Account Number: {self.account_number}\n'
            f'Savings Account Holder: {self.account_holder}\n'
            f'Savings Account Balance: ${self._balance:.2f}\n'
            f'Interest Rate: {self.interest_rate:.2f}%'
        )
    
## CURRENT ACCOUNT (INHERITANCE)
class CurrentAccount(Account):
    """A current account with an overdraft limit."""
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        """Initialize the current account with an overdraft limit."""
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit  

    @transaction_logger
    def withdraw(self, amount):
        """Withdraw money from the current account, considering the overdraft limit"""
        if amount > 0 and amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            print(f'${amount:.2f} withdrawn. New Balance: ${self._balance:.2f}')
        else:
            print('Error: Overdraft limit exceeded.')

    def display(self):
        """Display the current account details, including the overdraft limit"""
        print(
            f'Current Account Number: {self.account_number}\n'
            f'Current Account Holder: {self.account_holder}\n'
            f'Current Account Balance: ${self._balance:.2f}\n'
            f'Overdraft Limit: ${self.overdraft_limit:.2f}'
        )

## MULTIPLE INHERITANCE 
class PremiumAccount(SavingsAccount, LoanApplication):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance, interest_rate)
    
    def display(self):
        print(f'[Premium] Acc: {self.account_number}, Balance: {self._balance}, Perks Enabled.')


print('\n---SAVINGS ACCOUNT---')
sa = SavingsAccount('DBS-9876', 'Alfred Tan', 500_000, 5)
sa.deposit(10_000)
sa.withdraw(5000)
sa.add_interest()
sa.display()

ca = CurrentAccount('DBS-6543', 'Yew Leong', 700_000, 100_000)
ca.withdraw(550_000)
ca.display()

pa = PremiumAccount('DBS-8765', 'E-Patsy', 300_0000, 0)
pa.apply_loan(100_000)
pa.display()
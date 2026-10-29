class NegativeValueError(Exception):
    """Exception raised when an entered value is negative"""
    pass

class InsufficientFundsError(Exception):
    """Exception raised when an account balance drops below the transaction amount"""

    def __init__(self, balance, amount, message = "Transaction Declined"):
        self.balance = balance
        self.amount  = amount
        self.shortfall = amount - balance
        super().__init__(f"{message} (Balance: ${balance}, Requested: ${amount}, Shortfall: ${shortfall})")
def withdraw_money(balance, amount):
    if amount > balance:
        # Triggering the advanced exception with data payloads
        raise InsufficientFundsError(balance, amount)
    
    new_balance = balance - amount
    print(f"Withdrawal successful! Remaining balance: ${new_balance}")
    return new_balance

if __name__ == "__main__":
    account_balance = 100
    withdrawal_request = 150
    try:
        withdraw_money(account_balance, withdrawal_request)
    except InsufficientFundsError as error:
        print(f"Transaction Error: {error}")
        # Extracting the custom attributes attached to the exception object
        print(f"Logged Details -> Deficit amount: ${error.shortfall}")
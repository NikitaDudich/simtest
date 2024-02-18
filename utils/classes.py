class Transaction:
    def __init__(self, transaction_type: str, date, amount: str = None):
        self.transaction_type = transaction_type
        self.date = date
        self.amount = amount

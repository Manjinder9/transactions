class Transaction:

    def __init__(self, title, amount, type_of_transaction, note):
        self.title = title
        self.amount = amount
        self.type_of_transaction = type_of_transaction
        self.note = note

    def display_transaction(self):
        return f"Title: {self.title}, Amount: {self.amount}, Type: {self.type_of_transaction}, Note: {self.note}\n"

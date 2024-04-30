import json
from transaction import Transaction


class Statement:
    def __init__(self):
        self.statement = []

    def add_transaction(self, trans):
        self.statement.append(trans)

    def remove_transaction(self, title):
        for trans in self.statement:
            if trans.title == title:
                self.statement.remove(trans)
                return f"Removed {title}"
        return f"{title} not found"

    def display_transactions(self):
        if not self.statement:
            return f"No transactions available in your statement"
        return f"\n".join([trans.display_transaction() for trans in self.statement])

    def search_transaction(self, query_string):
        found = [trans for trans in self.statement if query_string.lower() in trans.title.lower()
                 or query_string.lower() in trans.type_of_transaction.lower()]
        if not found:
            return f"No Transaction found for {query_string}"
        return "\n".join([trans.display_transaction() for trans in found])

    def save_file(self, filename="wallet.json"):
        data = [{'Title': trans.title,
                 'Amount': trans.amount,
                 'Type_of_transaction': trans.type_of_transaction,
                 'Note': trans.note} for trans in
                self.statement]
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_file(self, filename="wallet.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.statement = [Transaction(trans['Title'],
                                              trans['Amount'],
                                              trans['Type_of_transaction'],
                                              trans['Note']) for trans in
                                  data]
        except FileNotFoundError:
            print("File not found")

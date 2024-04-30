# Main Program
from statement import Statement
from transaction import Transaction


def main():
    statement = Statement()
    # Looping user until exit.
    while True:
        print("\n==================Statement===================")
        print("1. Add Transaction")
        print("2. Remove Transaction")
        print("3. Display all Transactions")
        print("4. Search Transaction")
        print("5. Save Transaction to a file")
        print("6. Load Transaction from file")
        print("7. Exit")

        choice = int(input("Enter your choice 1- 7: "))
        if choice == 1:
            title = input("Enter your title of the transaction: ")
            amount = input("Enter Amount of the transaction: ")
            type = input("Enter your type of the transaction Expense/Deposit: ")
            note = input("Enter note to remember the transaction: ")
            transaction = Transaction(title, amount, type, note)
            statement.add_transaction(transaction)
            print(f"{title} has been added to the Statement")
            print(statement)

        elif choice == 2:
            title = input("Enter your title of the transaction: ")
            print(f"{statement.remove_transaction(title)}")

        elif choice == 3:
            print(f"{statement.display_transactions()}")

        elif choice == 4:
            query = input("Enter your search criteria: ")
            print(f"{statement.search_transaction(query)}")

        elif choice == 5:
            statement.save_file()
            print("File saved")

        elif choice == 6:
            statement.load_file()
            print("File loaded")

        elif choice == 7:
            print("Exiting program, Goodbye!!!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()

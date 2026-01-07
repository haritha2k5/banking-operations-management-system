import pandas as pd
import random
import sys

DATA_PATH = "data/bank.csv"


def load_data():
    try:
        return pd.read_csv(DATA_PATH, index_col="sno")
    except FileNotFoundError:
        print("Data file not found.")
        sys.exit(1)


def save_data(df):
    df.to_csv(DATA_PATH, index=True)


def create_account(df):
    sno = int(input("Enter serial number: "))
    name = input("Name: ")
    age = int(input("Age: "))
    phone = input("Phone (10 digits): ")

    if age < 18 or len(phone) != 10:
        print("Invalid age or phone number.")
        return

    acc_no = random.randint(10000, 99999)
    gender = input("Gender (M/F): ")
    balance = int(input("Initial deposit: "))
    address = input("Address: ")

    df.loc[sno] = [acc_no, name, age, gender, phone, balance, address]
    save_data(df)

    print("Account created successfully.")
    print("Account Number:", acc_no)


def deposit(df):
    sno = int(input("Enter serial number: "))
    amount = int(input("Amount to deposit: "))

    df.at[sno, "balance"] += amount
    save_data(df)
    print("Deposit successful.")


def withdraw(df):
    sno = int(input("Enter serial number: "))
    amount = int(input("Amount to withdraw: "))

    if df.at[sno, "balance"] < amount:
        print("Insufficient balance.")
        return

    df.at[sno, "balance"] -= amount
    save_data(df)
    print("Withdrawal successful.")


def view_account(df):
    sno = int(input("Enter serial number: "))
    print(df.loc[sno])


def menu():
    print("\n--- BANKING SYSTEM ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Account")
    print("5. Exit")


def main():
    df = load_data()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            create_account(df)
        elif choice == "2":
            deposit(df)
        elif choice == "3":
            withdraw(df)
        elif choice == "4":
            view_account(df)
        elif choice == "5":
            print("Exiting application.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

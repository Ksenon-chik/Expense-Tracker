import argparse
import json
from datetime import datetime


# Файл для хранения данных
DATA_FILE = "expenses.json"


# Функция для загрузки данных из файла
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Функция для сохранения данных в файл
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# Добавление расхода
def add_expense(description, amount):
    data = load_data()
    expense_id = len(data) + 1
    date = datetime.now().strftime("%Y-%m-%d")
    data.append({"id": expense_id, "date": date, "description": description, "amount": amount})
    save_data(data)
    print(f"Expense added successfully (ID: {expense_id})")


# Список всех расходов
def list_expense():
    data = load_data()
    print(f"{'ID':<5}{'Date':<12}{'Description':<20}{'Amount':<10}")
    print("-" * 50)
    for expense in data:
        print(f"{expense['id']:<5}{expense['date']:<12}{expense['description']:<20}${expense['amount']:<10}")


# Удаление расхода
def delete_expense(expense_id):
    data = load_data()
    updated_data = [expense for expense in data if expense["id"] != expense_id]
    if len(data) == len(updated_data):
        print("Expense not found!")
    else:
        save_data(updated_data)
        print(f"Expense deleted successfully (ID: {expense_id})")


# Сводка расходов
def summary(month=None):
    data = load_data()
    total = 0
    for expense in data:
        expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")
        if month is None or expense_date.month == month:
            total += expense["amount"]
    if month:
        print(f"Total expenses for month {month}: ${total}")
    else:
        print(f"Total expenses: ${total}")


# Парсинг аргументов командной строки
def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command")

    # Команда add
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, help="Description of the expense")
    add_parser.add_argument("--amount", type=float, required=True, help="Amount of the expense")

    # Команда list
    list_parser = subparsers.add_parser("list", help="List all expense")

    # Команда delete
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int, required=True, help="ID of the expense to delete")

    # Команда summary
    summary_parser = subparsers.add_parser("summary", help="Show summary of expenses")
    summary_parser.add_argument("--month", type=int, help="Show summary for a specific month (1-12)")

    # Разбор аргументов
    args = parser.parse_args()
    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "list":
        list_expense()
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "summary":
        summary(args.month)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

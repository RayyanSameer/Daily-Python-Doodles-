#Every SaaS product has a CRUD layer  create, read, update, delete data, persist it somewhere. This is a micro version of that. Backend interns spend their first weeks on exactly this kind of data handling. CSV processing also shows up constantly in DevOps for log exports and reports.

# A CLI app to track expenses by category. Add expenses, view totals per category, save to CSV, load back on next run.

import csv 
import os 

filename = "expenses.csv"

#Functions 
#Save to csv
#Load Csv

#Load Expenses 
def load_expenses():
    expenses = []
    if not  os.path.exists(filename):
        return expenses
    with open(filename,"r")as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses.append({
                "category": row["category"],
                "amount": float(row["amount"]),
                "note": row["note"]
            })
    return expenses

def save_expenses(expenses):
    with open(filename,"w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "amount", "note"])
        for expense in expenses:
            writer.writerow([expense["category"], expense["amount"], expense["note"]])

def add_expenses(expenses):
    category = input("Category: (food/transport/bills/other): ").strip().lower()
    try:
        amount = float(input("Enter a number "))
    except ValueError:
        print("Invalid")
        return
    note = input("Note: optional").strip()
    expenses.append({"category": category, "amount": amount, "note": note})
    print("Expense added")

def view_total(expenses):
    if not expenses:
        print("No expenses here! ")
        return
    totals = {}
    for expense in expenses:
        cat = expense["category"]
        amt = expense["amount"]
        if cat in totals:
            totals[cat] += amt
        else:
            totals[cat] = amt

    print("\n--- Totals by Category ---")
    for cat, total in totals.items():
        print(f"  {cat:<15} ${total:.2f}")    # 2 decimal places
    print(f"\n  {'TOTAL':<15} ${sum(totals.values()):.2f}")

if __name__ == "__main__":
    current_expenses = load_expenses()           # load on startup

    while True:
        print("\n[1] Add expense  [2] View totals  [3] Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_expenses(current_expenses)
            save_expenses(current_expenses)
        elif choice == "2":
            view_total(current_expenses)
        elif choice == "3":
            print("Bye.")
            break                         
        else:
            print("Invalid choice.")    



    

        
    
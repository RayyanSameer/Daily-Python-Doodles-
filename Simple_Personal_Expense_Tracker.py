#Simple Personal Expense Tracker that willlater be cloud hosted.
print("Daily Expense Tally")
food = int(input("Food: "))
transportation = int(input("Transit: "))
entertainment = int(input("Entertainment"))
shopping = int(input("Shopping: "))

all_expenses = {"Food": food,
                "Transportation" : transportation,
                "Entertainment: ": entertainment,
                "Shopping: ": shopping}

total = food + transportation + entertainment + shopping

highest_expense = max(all_expenses.values())
baseline = food + transportation + entertainment

print("Total :" + str(total))
print("Your highest expense today was : ",highest_expense)
print(f"Your baseline costs would amount to : {baseline * 30} over a period of 30 days")

print("Percentage wise breakdown: ")

food_percentage = (food / total) * 100
transportation_percentage = (transportation / total) * 100
entertainment_percentage = (entertainment / total) * 100
shopping_percentage = (shopping / total) * 100

print(f"  Food: {food_percentage:.2f}%")
print(f"  Transportation: {transportation_percentage:.2f}%")
print(f"  Entertainment: {entertainment_percentage:.2f}%")
print(f"  Shopping: {shopping_percentage:.2f}%")

income = int(input("Whats your income ?: "))
savings = income -baseline
print(f"With this expense , expect { savings } at the end of the month")
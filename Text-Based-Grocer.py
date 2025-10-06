#Simple Text based grocey sorter
#day 1
groceies = {"Milk":24 ,"Cheese":53,"Eggs":8 ,"Curd":48,"Bread":40}
list = {}

print("Available Groceries:")
print("Bread - 40Rs")
print("Milk - 24Rs")
print("Cheese - 53Rs")
print("Curd - 48Rs")
print("Eggs - 8Rs")

while True :
        print("What are you looking for today? Type 'done' to finish")
        ans = input().lower()

        if ans == 'done':
            break

        if ans in groceies:
            print("Thats in stock,how many?")
            qty = input()
            cart ={ans : qty }

        if ans in cart:
            print("You already bought that :/")
            cart[ans] = qty
        else:
            print("Dont have any")    


print("Summary")
for item , quantity in cart.items():
    print(f"-{item.title()}:{quantity}")

total = 0
for item , quantity in cart.items():
    price = groceies[item]
    cost = price * quantity
    total =+ cost
    print(total)



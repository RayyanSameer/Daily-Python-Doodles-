#Inventory manager 

items = [] #item stores dictionaries of items each with item , item USN , qty , price 

#Operations that can be done 
# 1) Add items , price , qty in stock , USN
# 2) Delete items , price , qty in stock , USN
# 3) View items , price , qty in stock , USN
# 4) Update items , price , qty in stock , USN
# 5) Search items 
# 6) Exit 

#Menu 

while True:
    print("Welcome to inventory manager !")
    print(""" 1) Add items , price , qty in stock , USN 
 2) Delete items
 3) View items 
 4) Update items
 5) Search items 
 6) Exit""")
    
    choice = input("Enter your choice: ")
    if choice == 1:
        number_of_entries = input(int("Enter how many items you wanna add"))
        inc_count = 0
        for i in range(number_of_entries):
            item = input("Enter item name: ")
            item_usn = input("Enter item usn code ")
            qty = input("Enter total input: ")
            price = input("Enter unit price : ")

            items.append[{"item":item,
                          "item_usn":item_usn,
                          "qty": qty,
                          "price":price}]
        if choice == 2:
            target = input("What would you like to remove ?: ")
            found == False
            for items in items:
                if items["item"] == target:
                    items.remove(target)
                    price(f"{target} has been removed :)")
                    found = True 
                else:
                    print("Not found !")
        if choice == 3:
            print(items)
        if choice == 4:
            target_update = input("What would you like to update ?: ")
            found == False
            for items in items:
                if items["item"] == target:
                    item = input("Enter item name: ")
            item_usn = input("Enter item usn code ")
            qty = input("Enter total input: ")
            price = input("Enter unit price : ")

            items[target_update] = [{"item":item,
                          "item_usn":item_usn,
                          "qty": qty,
                          "price":price}]
        if choice == 5:
            target_search = input("What would you like to search ?: ")
            found == False
            for items in items:
                if items["item"] == target:
                    print(items)
                else:
                    print("Not found ")   
        if choice == 6:
            quit()             




        

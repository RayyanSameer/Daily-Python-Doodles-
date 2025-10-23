from functools import reduce

raw_data_expenses = ["12000","253.52","misc","200"]

#Filter invalid data using filter()
#Keep only numbers 

clean = list(filter(lambda x: x.replace('.',"",1).isdigit(),raw_data_expenses))
print(clean)

#String --> Float4
#Use map
convert = list(map(float, clean))
print(convert)

#Filter large expense
large_expense = list(filter(lambda x: x>1000, convert))
print(large_expense)

#Sum
sum = reduce(lambda a,b : a+b,convert)
avg = sum/len(convert)
print("Total", sum)
print("Average: ",avg)

print("Cleaned data:", convert)
print("Expenses > 1000:", large_expense)
print(f"Total = ₹{sum:.2f}")
print(f"Average = ₹{avg:.2f}")
rent = int(input("enter the total rent of room :"))

food = int(input("food expense of month :"))

electricity_bill_permonth = int(input("enter the electricity bill of month :"))

charge_per_unit = int(input("enter the price of per unit :"))

person = int(input("enter number of person in room :"))

total_bill = electricity_bill_permonth + charge_per_unit

output = (rent + food + total_bill) // person

print("each person will pay =", output)

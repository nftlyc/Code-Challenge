# Grocery

name = input("Enter your name: ")
grocery = input("Did you buy grocery? (yes / no): ")

if grocery.lower() == "yes":
	name_item = input("Enter the name of the item you buy: ")
	price_item = eval(input("Enter the amount of the item: "))
	age = eval(input("Enter your age: "))
	given_amount = eval(input("Amount given: "))

	disc = round((price_item * 0.052), 2)
	discprice = round((price_item - disc), 2)
	tax = round((price_item * 0.123), 2)
	taxprice = round((price_item - disc), 2)

	if age >= 60:
		print(f"Hi {name}, you purchased a {name_item}, with a price of {price_item} pesos plus a 5.2% discount ({disc}pesos) to your total purchase.")
		print(f"Total of : {round((price_item - disc), 2)}")
		print(f"Change : {round((given_amount - discprice), 2)}")
		print("Thanyou for your purchase \nCome back again.")
		
	elif age < 60:
		print(f"Hi {name}, you purchased a {name_item}, with a price of {price_item} pesos plus a 12.3% tax {tax} pesos to your total purchase. ")
		print(f"Total of : {round((price_item + tax), 2)}")
		print(f"Change : {round((given_amount - taxprice), 2)}")
		print("Thanyou for your purchase \nCome back again.")

		
else:
	print("Thanyou for trusting us\nSee you again next time")


	
	
		

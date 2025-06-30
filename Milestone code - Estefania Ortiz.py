"""
File: Prove 4

Author: Estefanía Ortiz

Description: Milestone code Final

"""
# pi = 3.14159
# print(pi)

print("What is the price of a child's meal? ")
num1 = 3.562342
a = round(num1,2)
print(f"The price of a child's meal is ${a}")

print("What is the price of a adult's meal? ")
num2 = 6.956235
b = round(num2,2)
print(f"The price of a adult's meal is ${b}") 

adults = input("How many adults are there? ")

children = input("How many children are there? ")

print("What is the sales tax rate? ")
porc = float(input())

print("Subtotal ")
Subt = ((float(adults) * float(b)) + (float(children) * float(a)))
print(f"{Subt}")
sales_tax_rate = porc * Subt /100
print("Sales tax ")
Sales_Tx = round(sales_tax_rate,2)
print(f"${Sales_Tx}")

print("Total")
Total = round(Subt + Sales_Tx,2)
print(f"${Total}")

print("What is the payment amount?")
payment_amount = input()
print("Change")
Chang = (float(payment_amount) - float(Total))
print(f"${Chang}")
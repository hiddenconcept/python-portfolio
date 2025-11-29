print("Welcome to Python Pizza Deliveries!")

# Get pizza size and assign price
size = input("What size pizza do you want? S, M, L, or XL: ").upper()
if size == "S":
    print("Your size is Small")
    size_price = 10
elif size == "M":
    print("Your size is Medium")
    size_price = 13
elif size == "L":
    print("Your size is Large")
    size_price = 14
elif size == "XL":
    print("Your size is Extra Large")
    size_price = 20
else:
    print("Invalid size! Defaulting to Small")
    size_price = 10

# Pepperoni
pepperoni = input("Do you want delivery? Y/N or Yes/No: ").strip().upper()

# Validate input
while pepperoni not in ["Y", "YES", "N", "NO"]:
    pepperoni = input("Invalid choice! Please type 'Y', 'N', 'Yes', or 'No': ").strip().upper()
if pepperoni == "Y":
    print("Extra pepperoni added.")
    pepperoni_price = 1.5
else:
    pepperoni_price = 0


# Extra cheese
extra_cheese = input("Do you want delivery? Y/N or Yes/No: ").strip().upper()

# Validate input
while extra_cheese not in ["Y", "YES", "N", "NO"]:
    extra_cheese = input("Invalid choice! Please type 'Y', 'N', 'Yes', or 'No': ").strip().upper()
if extra_cheese == "Y":
    print("Extra cheese added.")
    cheese_price = 1.5
else:
    cheese_price = 0

delivery = input("Do you want delivery? Y/N or Yes/No: ").strip().upper()

# Validate input
while delivery not in ["Y", "YES", "N", "NO"]:
    delivery = input("Invalid choice! Please type 'Y', 'N', 'Yes', or 'No': ").strip().upper()

if delivery == "Y":
    print("Delivery added.")
    delivery_fee = 8.99
else:
    delivery_fee = 0

tax_percentage = 13
tax = 1.13

# Calculate total bill
bill_total_tax = (size_price + pepperoni_price + cheese_price + delivery_fee) * tax
bill_total = (size_price + pepperoni_price + cheese_price + delivery_fee)

print("")
print("")
print("")
print("Receipt:")
print("Python Pizza ")
print("")
print("123 Python Lane")
print("")
print("1-800-666-1337")
print("")
print("______________")
print(f"Pizza size: ${size_price:.2f}")
print(f"Pepperoni: ${pepperoni_price:.2f}")
print(f"Extra cheese: ${cheese_price:.2f}")
print(f"Delivery fee: ${delivery_fee:.2f}")
print(f"Total (without tax): ${bill_total:.2f}")
print(f"Tax (%): {tax_percentage:.2f}")  # show as percentage
print("")

# Display total
print(f"Your total is: ${bill_total_tax:.2f}")

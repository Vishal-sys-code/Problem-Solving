print("Return Statements")
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return tax

price = value_added_tax(100)
print(price)
print(type(price))


""" Without any return statement the python will return a NONE."""

def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return amount, tax, total_amount

price = value_added_tax(100)
print(price, type(price)) # Tuple

# ---------------------------------------

def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return [amount, tax, total_amount]

price = value_added_tax(100)
print(price, type(price)) # List
print(price[1])

# ---------------------------------------

def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return {amount, tax, total_amount}

price = value_added_tax(100)
print(price, type(price)) # Set

# ---------------------------------------

def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return f"{amount}, {tax}, {total_amount}"

price = value_added_tax(100)
print(price, type(price)) # Set
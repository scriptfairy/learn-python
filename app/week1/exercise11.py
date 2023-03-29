# Exercise 11: # Create a function in Python that accepts two parameters. The first
# should be the full price of an item as an integer. The second should be the discount
# percentage as an integer. Return the price of the item after the discount has been
# applied

import decimal

def calculate_discounted_price(full_price, discount):
    # Use decimal to garantee the return value will always have 2 decimal points
    discounted_price = decimal.Decimal(full_price - (full_price * discount / 100))
    formatted_price = round(discounted_price,2)
    return formatted_price

full_price = 100
discount = 20
discounted_price = calculate_discounted_price(full_price, discount)
print(discounted_price) 
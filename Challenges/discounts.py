from functools import partial

prices = [
    10.50,
    9.99,
    0.25,
    1.50,
    8.79,
    101.25,
    8.00
]


def discount(price, amount):
    return price - price * (amount/100)

# First, import partial from functools
# Now use partial to make a version of discount that applies 10% discount
# Name this partial function discount_10
discount_10 = partial(discount, amount=10)

# Follow that same pattern to make discount_25 and discount_50
discount_25 = partial(discount, amount=25)
discount_50 = partial(discount, amount=50)

# Finally, I need to see all prices with each discount applied
# Use map to create prices_10, prices_25, and prices_50
prices_10 = map(discount_10, prices)
prices_25 = map(discount_25, prices)
prices_50 = map(discount_50, prices)
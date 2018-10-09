from operator import add
from functools import reduce

prices = [
    (6.99, 5),
    (2.94, 15),
    (156.99, 2),
    (99.99, 4),
    (1.82, 102)
]

# We have a bunch of prices and sales numbers and wee need to find out our total earnings.
# Let's start by writing a function named product_sales that takes a single two-member tuple made up of a price
# and a number of units sold.
# product_sales should return the product of the price and the number of units

def product_sales(info):
    return info[0] * info[1]

# We need to add two numbers together.
# We could write a function that does this but that seems silly.
# Import add from the operator module.
# Import reduce() from functools

# We're ready to find out totals
# Create a variable named total
# Use map() to find the per-product totals for each item in prices
# Then use reduce(and add) to find the total value

total = reduce(add, map(product_sales, prices))
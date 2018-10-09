dimensions = [
    (5, 5),
    (10, 10),
    (2.2, 2.3),
    (100, 100),
    (8, 70),
]

# Create a function named area() trhat takes a single argument which will be a two_member tuple
# area() should return result of multiplying first item in tuple by second in tuple
def area(iter1):
    for i in iter1:
        return iter1[0] * iter1[1]

# Now make a variable named areas that calculates the area of each item in dimensions using area function
# You should do this with list comprehension
areas = [area(specs) for specs in dimensions]
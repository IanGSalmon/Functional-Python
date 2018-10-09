# Import itemgetter from the operator module
# Now create a variable named sorted_fruit that used sorted() and itemgetter() to sort fruit_list by the second item in each tuple
from operator import itemgetter


fruit_list = [
    ('apple', 2),
    ('banana', 5),
    ('coconut', 1),
    ('durian', 3),
    ('elderberries', 4)
]

sorted_fruit = sorted(fruit_list, key=itemgetter(1))
print(sorted_fruit)
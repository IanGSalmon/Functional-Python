backwards = [
    'tac',
    'esuoheerT',
    'htenneK',
    [5, 4, 3, 2, 1],
]

# Create a function named reverse that takes a single iterable item and returns a reversed version of that item
def reverse(my_list):
    return my_list[::-1]

# Now use map() to create a cariable named forwards
# forwards should use reverse() to reverse the order of every item in backwards
# I put it in a list so I could call print and view output
forwards = list(map(reverse, backwards))
print(forwards)
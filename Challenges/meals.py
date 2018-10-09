meals = [
    {'name': 'cheeseburger',
     'calories': 750},
    {'name': 'cobb salad',
     'calories': 250},
    {'name': 'large pizza',
     'calories': 1500},
    {'name': 'burrito',
     'calories': 1050},
    {'name': 'stir fry',
     'calories': 625}
]

# Use a lambda and filter() to create a variable named high_cal
# with only the items in meals where "calories" is greater than 1000
high_cal = filter(lambda meal: meal['calories'] > 1000, meals)
words = [
    'yellow',
    'red',
    'yesterday',
    'tomorrow',
    'maybe',
    'zucchini',
    'eggplant',
    'year',
    'month',
    'yell',
    'yonder',
    'today',
]

# Create a variable named y_words that uses a list comprehension 
# to only contain the words from words that start with the letter 'y'
y_words = [options for options in words if options.startswith('y')]
print(y_words)
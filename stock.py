import json
from copy import copy
from operator import attrgetter, itemgetter
from functools import reduce, partial

class Book:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return str(self)
    
    
def get_books(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]
    
BOOKS = get_books('books.json')
RAW_BOOKS = get_books('books.json', raw=True)

#important_list = [5, 3, 1, 2, 4]
# important_list.sort() , BAD IDEA, sorts list in place
# sorted(important_list), GOOD, sorts a copy of the list
#print(sorted(important_list))
#print(important_list)

# itemgetter is looking up by index
# pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
#print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])

# attrgetter is looking up by attribute
#pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'))
#print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages)

# map() takes function and iterable, returns new iterable w/ mutated values
#a = [1, 2, 3]
#def double(n):
#    return n * 2
#print(list(map(double, a)))

# Function which will be called for map() and list comprehension examples
# Often start with 'apply' as naming convention when using map()
def apply_sales_price(book):
    """Apply a 20% discount to book's price"""
    book = copy(book)
    book.price = round(book.price-book.price*.2, 2)
    return book

# Using map
sales_books = list(map(apply_sales_price, BOOKS))
# Using list comprehension
sales_books2 = [apply_sales_price(book) for book in BOOKS]
#print(BOOKS[0].price)
#print(sales_books[0].price)
#print(sales_books2[0].price)


### FILTER ###
# Function which will be called for filter() and list comp examples
# Often start with 'is' as naming convention when using filter()
def is_long_book(book):
    """Does a book have 600+ pages"""
    return book.number_of_pages >= 600

# Using filter()
long_books = list(filter(is_long_book, BOOKS))
# Using list comprehension
long_books2 = [book for book in BOOKS if book.number_of_pages >= 600]
#print(len(BOOKS))
#print(len(long_books))
#print(len(long_books2))


### CHAINING ###
def has_roland(book):
    # any returns True is ANYTHING is truthy in list comp
    return any(["Roland" in subject for subject in book.subjects])

def titlecase(book):
    book = copy(book)
    # title() is titlecase, 1st letter cap
    book.title = book.title.title()
    return book

# have to map first, bc we need to titlecase before filtering for "Roland"
#print(list(map(titlecase, filter(has_roland, BOOKS))))

def is_good_deal(book):
    return book.price <= 5

cheap_books = sorted(
    filter(is_good_deal, map(apply_sales_price, BOOKS)),
    key=attrgetter('price')
)
#print(cheap_books[0])
#print(cheap_books[0].price)

### REDUCE ###
# This is a function we can use with functools.reduce()
def product(x, y):
    return x * y

#print(reduce(product, [1, 2, 3, 4, 5]))

# This is another function we can use with functools.reduce()
def add_book_prices(book1, book2):
    return book1 + book2

total = reduce(add_book_prices, [b.price for b in BOOKS])
#print(total)


# This is the LONG way to make the recursion
def long_total(a=None, b=None, books=None):
    if a is None and b is None and books is None:
        return None
    if a is None and b is None and books is not None:
        a = books.pop(0)
        b = books.pop(0)
        return long_total(a, b, books)
    if a is not None and books and books is not None and b is None:
        b = books.pop(0)
        return long_total(a, b, books)
    if a is not None and b is not None and books is not None:
        return long_total(a+b, None, books)
    if a is not None and b is not None and not books:
        return long_total(a+b, None, None)
    if a is not None and b is None and not books or books is None:
        return a

#print(long_total(None, None, [b.price for b in BOOKS]))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#print(factorial(5))


### LAMBDA ###
total = reduce(lambda x, y: x + y, [b.price for b in BOOKS])
#print(total)
long_books = filter(lambda book: book.number_of_pages >= 600, BOOKS)
#print(len(list(long_books)))
good_deals = filter(lambda book: book.price <= 6, BOOKS)
#print(len(list(good_deals)))

### PARTIALS ###
def mark_down(book, discount):
    book = copy(book)
    book.price = round(book.price-book.price*discount, 2)
    return book

standard = partial(mark_down, discount=.2)
half = partial(mark_down, discount=.5)
half_price_books = map(half, filter(is_long_book, BOOKS))
#print(list(half_price_books))

### CURRYING ###
# Good if you have to wait on future input
def curried_f(x, y=None, z=None):
    def f(x, y, z):
        return x**3 + y**2 + z

    if y is not None and z is not None:
        return f(x, y, z)
    if y is not None:
        return lambda z: f(x, y, z)
    
    return lambda y, z=None: (
        f(x, y, z) if (y is not None and z is not None)
        else(lambda z: f(x, y, z))
    )

print(curried_f(2, 3, 4))
g = curried_f(2)
print(g)
h = g(3)
print(h)
i = h(4)
print(i)
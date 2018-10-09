very_important_list = [5, 2, 3, 1]
name = 'Kenneth'

# This changes the list outside of the function's scope, BAD
def mutate():
    very_important_list.sort()

# Global looks for something outside of function's defined scope
# This function changes the 'name' variable which is outside its scope
def global_use():
    global name
    name = 'James'

# This function is TOO LONG
def long_func():
    import random
    some_nums = random.shuffle(range(5, 250))
    for index, num in enumerate(some_nums):
        if num % 3:
            some_nums[index] = num ** 5
        elif num % 7:
            some_nums[index] = num ** 10
        else:
            some_nums[index] = num ** 2
    total = sum(some_nums)
    print("The total of the numbers is {}".format(total))
    return some_nums

# Taking unnecessary inputs
# Some of these details are unused
def lot_of_inputs(player_1, player_2, score_1, score_2,
                  when=None, where=None, teams=False):
    from collections import namedtuple
    player = namedtuple('Player', ['name', 'score'])
    score = namedtuple('Score', ['player1', 'player2'])
    p1 = player(player_1, score_1)
    p2 = player(player_2, score_2)
    return score(p1, p2)